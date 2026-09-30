#!/usr/bin/env python3
"""SCAP English/Tamil/Sinhala chapter coverage and selected financial-figure parity."""
import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ("01-Fundamental-Analysis", "02-Technical-Analysis")
NAMES = ("README.md", "VISUAL-REPORT.md", "SWOT-ANALYSIS.md")
LANGUAGES = ("en", "ta", "si")
DECIMAL = re.compile(r"(?<![A-Za-z0-9/])([−+\-]?\d{1,3}(?:,\d{3})+(?:\.\d+)?|[−+\-]?\d+\.\d{1,3})(%|m|bn)?(?![A-Za-z0-9/])")
URL = re.compile(r"https?://\S+")
MDLINK = re.compile(r"!?\[([^\]]*)\]\([^)\n]*\)")


def langfile(lang, common, root=ROOT):
    return Path(root) / (("" if lang == "en" else lang + "/") + common)


def without_navigation(text):
    text = URL.sub("", text)
    text = MDLINK.sub(lambda match: match.group(1), text)
    text = re.sub(r"^\s*#.*$", "", text, flags=re.M)
    return text.replace("\u2212", "-").replace("\u2013", "-")


def numeric_tokens(text):
    found = set()
    for match in DECIMAL.finditer(without_navigation(text)):
        plain = match.group(1).replace(",", "").replace("+", "")
        try:
            value = float(plain)
        except ValueError:
            continue
        if 1900 <= abs(value) <= 2100 and value.is_integer():
            continue
        if abs(value) < 100 and not match.group(2):
            continue
        found.add((round(value, 4), match.group(2) == "%"))
    return found


def english_chapters(root=ROOT):
    paths = set()
    for group in FOLDERS:
        for path in (Path(root) / group).glob("*/*.md"):
            if path.name in NAMES:
                paths.add(path.relative_to(root).as_posix())
    return sorted(paths)


def check(root=ROOT, ledger=None):
    root = Path(root)
    facts = json.loads(Path(ledger or root / "data/financial-facts.json").read_text(encoding="utf-8"))
    errors, warnings = [], []
    chapters = english_chapters(root)
    if sum(p.endswith("/README.md") for p in chapters) != 20:
        errors.append("Expected exactly 20 English research chapter READMEs")
    for common in chapters:
        texts = {}
        for lang in LANGUAGES:
            path = langfile(lang, common, root)
            if not path.is_file():
                errors.append(f"{common}: missing {lang} translation")
            else:
                text = path.read_text(encoding="utf-8")
                texts[lang] = text
                if not text.strip():
                    errors.append(f"{common}: empty {lang} translation")
        if len(texts) != 3:
            continue
        counts = {lang: len(re.findall(r"^\s*\x60{3}mermaid\b", t, flags=re.M)) for lang, t in texts.items()}
        if len(set(counts.values())) != 1:
            errors.append(f"{common}: Mermaid chart count differs across languages {counts}")
        for literal in facts.get("translation_required", {}).get(common, []):
            for lang, content in texts.items():
                normalized = content.replace("\u2212", "-").replace("\u2013", "-")
                normalized_literal = literal.replace("\u2212", "-").replace("\u2013", "-")
                if not re.search(r"(?<![0-9.,+-])" + re.escape(normalized_literal) + r"(?![0-9,.%])", normalized):
                    errors.append(f"{common}: {lang} missing required financial figure {literal}")
        english = numeric_tokens(texts["en"])
        for lang in ("ta", "si"):
            local = numeric_tokens(texts[lang])
            only_en, only_local = sorted(english - local), sorted(local - english)
            if only_en or only_local:
                warnings.append(
                    f"{common}: check {lang} quantitative text: English-only {only_en[:5]}, "
                    f"{lang}-only {only_local[:5]}; may reflect a legitimate prose difference."
                )
    return chapters, errors, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        chapters, errors, warnings = check(args.root)
    except (OSError, ValueError, KeyError) as exc:
        print("::error title=Translation consistency::" + str(exc))
        return 1
    for message in errors:
        print("::error title=Translation figure or coverage::" + message.replace("%", "%25"))
    for message in warnings[:30]:
        print("::warning title=Review translation figures::" + message.replace("%", "%25"))
    report = (f"### Trilingual consistency\n\nEnglish chapters: {len(chapters)}; "
              f"blocking defects: **{len(errors)}**; possible additional numeric drift: "
              f"**{len(warnings)}** (first 30 shown). Semantic translation accuracy requires manual review.\n")
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(report)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
