#!/usr/bin/env python3
"""SCAP static research gates; original facts must still be reviewed by a human."""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^)\s]+)")
HTML_LINK = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.I)
FENCE = re.compile(r"^[ \t]{0,3}(\x60{3,}|~{3,})(.*)$")
CLAIM = re.compile(r"\b(?:LKR|Rs\.?|USD)\s*[\d,.]+|\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b|\b\d+(?:\.\d+)?\s*%|\b(?:PAT|CAR|NPL|EPS|GWP|debt|borrowings?)\b.{0,24}\b\d+(?:\.\d+)?", re.I)
SOURCE = re.compile(r"\]\((?:https?://|(?:\.\./)*sources/records/|(?:\.\./)*SOURCES\.md)|\bSource(?:s)?\s*/\s*status\s*:", re.I)
ARTICLE = re.compile(r"^(?:ta/|si/)?(?:01-Fundamental-Analysis|02-Technical-Analysis)/[^/]+/(?:README|VISUAL-REPORT|SWOT-ANALYSIS)\.md$|^(?:ta/|si/)?reports/[^/]+\.md$")
DIAGRAM = re.compile(r"^(?:flowchart|graph|xychart-beta|pie|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?|erDiagram|gantt|gitGraph|timeline|mindmap|quadrantChart|journey|sankey-beta|block-beta|architecture-beta|requirementDiagram|C4Context)\b")
FIELDS = {
    "source id": ("source id", "stable source id"),
    "publisher": ("publisher",),
    "reporting period": ("period covered", "reporting/announcement period"),
    "entity/scope": ("reporting entity / accounting scope", "legal entity and scope"),
    "audit/status": ("audit / evidence status", "verification status"),
    "page/section": ("page references / section", "original page/section"),
    "redistribution permission": ("redistribution permission",),
    "sha-256/status": ("sha-256", "original sha-256 / size"),
}


class Results:
    def __init__(self):
        self.errors = 0
        self.warnings = 0
        self.links = 0
        self.documents = 0
        self.records = 0
        self.diagrams = 0

    def report(self, file, line, kind, title, message):
        if kind == "error":
            self.errors += 1
        else:
            self.warnings += 1
        path = file.relative_to(ROOT).as_posix() if file.is_relative_to(ROOT) else str(file)
        message = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::{kind} file={path},line={max(1,line)},title={title}::{message}", flush=True)


def changed_markdown(base):
    if not base or base == "0" * 40:
        base = "HEAD^"
    try:
        result = subprocess.check_output(
            ["git", "diff", "--name-only", "-z", "--diff-filter=ACMR", base, "HEAD", "--"],
            cwd=ROOT)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError("Unable to determine changed files against " + base) from exc
    return [ROOT / os.fsdecode(x) for x in result.split(b"\0") if x.endswith(b".md")]


def clean_code_and_export(path, content, output_dir, out):
    clean, opened, chart = [], None, []
    for n, line in enumerate(content.splitlines(keepends=True), 1):
        fence = FENCE.match(line.rstrip("\r\n"))
        if opened is None:
            if fence:
                opened = (fence.group(1)[0], len(fence.group(1)), fence.group(2).strip().lower(), n)
                chart = []
                clean.append("\n")
            else:
                clean.append(line)
        elif fence and fence.group(1)[0] == opened[0] and len(fence.group(1)) >= opened[1] and not fence.group(2).strip():
            if opened[2].split()[:1] == ["mermaid"]:
                out.diagrams += 1
                code = "".join(chart).strip()
                if not code or not DIAGRAM.match(code):
                    out.report(path, opened[3], "error", "Mermaid", "Empty or invalid Mermaid chart type")
                elif output_dir is not None:
                    output_dir.mkdir(parents=True, exist_ok=True)
                    label = re.sub(r"[^a-zA-Z0-9_.-]", "_", str(path.relative_to(ROOT)))
                    (output_dir / f"{label}-{opened[3]}.mmd").write_text(code + "\n", encoding="utf-8")
            opened = None
            chart = []
            clean.append("\n")
        else:
            chart.append(line)
            clean.append("\n")
    if opened:
        out.report(path, opened[3], "error", "Mermaid", "Unclosed fenced code block")
    return "".join(clean)


def validate_links(path, content, out):
    for n, line in enumerate(content.splitlines(), 1):
        for m in list(LINK.finditer(line)) + list(HTML_LINK.finditer(line)):
            raw = m.group(1).strip().strip("<>")
            if not raw or raw.startswith(("#", "//", "mailto:", "tel:", "data:")):
                continue
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
                continue
            out.links += 1
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT.resolve()):
                out.report(path, n, "error", "Markdown links", "Relative link escapes repository: " + raw)
            elif not resolved.exists():
                out.report(path, n, "error", "Markdown links", "Broken local link: " + raw)


def validate_citations(path, content, out):
    if not ARTICLE.fullmatch(path.relative_to(ROOT).as_posix()):
        return
    lines = content.splitlines()
    numbers = [n for n, line in enumerate(lines, 1)
               if not line.lstrip().startswith(("#", "|", "<", "[", ">", "- [ ]", "- [x]"))
               and CLAIM.search(line)]
    if not numbers:
        return
    if not SOURCE.search(content):
        out.report(path, numbers[0], "error", "Missing citations",
                   "Quantitative research contains no issuer URL or source-record link")
        return
    warnings = 0
    for n in numbers:
        nearby = "\n".join(lines[max(0, n - 4):min(len(lines), n + 4)])
        if not SOURCE.search(nearby) and warnings < 20:
            out.report(path, n, "warning", "Citation proximity",
                       "Quantitative claim has no nearby source link; check editorially")
            warnings += 1


def fields_of(text):
    fields = {}
    for line in text.splitlines():
        if line.startswith("|"):
            parts = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(parts) > 1:
                fields[re.sub(r"[\x60*_]", "", parts[0]).strip().lower()] = parts[1]
    return fields


def validate_record(file, out):
    text = file.read_text(encoding="utf-8")
    values = fields_of(text)
    out.records += 1
    for name, aliases in FIELDS.items():
        value = next((values[key] for key in aliases if key in values), "")
        if not value or value.strip() in ("-", "—", "______"):
            out.report(file, 1, "error", "Source records", "Missing required source field: " + name)
        if name == "source id" and value and value.strip().strip("\x60") != file.stem:
            out.report(file, 1, "error", "Source records", "Stable source ID does not match filename")
    original = values.get("original url") or re.search(r"\*\*Original document:\*\*[^\n]+", text)
    if not original or not re.search(r"https?://\S+", str(original)):
        out.report(file, 1, "error", "Source records", "Missing original publisher URL")
    if re.search(r"Original document copied into repository:\*\* \*\*YES", text, re.I):
        sha = values.get("sha-256") or values.get("original sha-256 / size") or ""
        if not re.search(r"\b[a-f0-9]{64}\b", sha, re.I):
            out.report(file, 1, "error", "Source records", "Archived original requires SHA-256")
        if not any((ROOT / "sources/documents" / (file.stem + ext)).is_file()
                   for ext in (".pdf", ".csv", ".xlsx")):
            out.report(file, 1, "error", "Source records", "Claimed original binary is missing")


def check_register(out):
    register = ROOT / "sources/SOURCE-REGISTER.md"
    folder = ROOT / "sources/records"
    if not register.is_file() or not folder.is_dir():
        out.report(register, 1, "error", "Source records", "Source register or records directory missing")
        return
    body = register.read_text(encoding="utf-8")
    for record in folder.glob("*.md"):
        if "records/" + record.name not in body:
            out.report(register, 1, "error", "Source records", "Unregistered source " + record.name)
        validate_record(record, out)
    for match in re.findall(r"\[View evidence\]\((records/[^)#]+\.md)\)", body):
        if not (ROOT / "sources" / match).is_file():
            out.report(register, 1, "error", "Source records", "Missing listed record: " + match)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="HEAD^")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--mermaid-dir", type=Path, default=None)
    a = parser.parse_args()
    out = Results()
    try:
        files = list(ROOT.rglob("*.md")) if a.all else changed_markdown(a.base)
    except RuntimeError as exc:
        print("::error title=Diff::" + str(exc))
        return 2
    for file in sorted(set(files)):
        if not file.is_file() or file.suffix != ".md" or "node_modules" in file.parts or ".git" in file.parts:
            continue
        out.documents += 1
        body = file.read_text(encoding="utf-8")
        text = clean_code_and_export(file, body, a.mermaid_dir, out)
        validate_links(file, text, out)
        validate_citations(file, text, out)
    check_register(out)
    summary = (
        "## SCAP research validation\n\n"
        f"- Mode: {'all Markdown' if a.all else 'changed Markdown plus all source records'}\n"
        f"- Documents: {out.documents}; links checked: {out.links}; Mermaid charts extracted: {out.diagrams}\n"
        f"- Source records schema checked: {out.records}\n"
        f"- Blocking errors: **{out.errors}**; citation review warnings: **{out.warnings}**\n"
        "- External publisher URLs and accounting truth need separate human verification.\n"
        "- Mermaid chart grammar is rendered by the official CLI after this Python check.\n"
    )
    print(summary)
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as file:
            file.write(summary + "\n")
    return 1 if out.errors else 0


if __name__ == "__main__":
    sys.exit(main())
