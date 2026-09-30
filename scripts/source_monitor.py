#!/usr/bin/env python3
"""Source watch: check public issuer/CSE HTML links; open Issues for newly found real SCAP PDFs."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
AGENT = "SCAP-Public-Research-Watch/1.0"
YEAR = re.compile(r"(2025[\-/ _]+2026|2026[\-/ _]+2027|\b2026\b|\b2027\b)", re.I)
CSE_LINK = re.compile(r"https?://[^\s\"'<>)]+?\.pdf(?:\?[^\"'<>\s]+)?", re.I)
MARKER = "SCAP_SOURCE_SHA256:"


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.recent = []
        self.active = None
        self.matches = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.active = {"href": dict(attrs).get("href", ""),
                           "label": " ".join(self.recent[-5:]), "title": ""}

    def handle_data(self, content):
        content = " ".join(content.split())
        if content:
            if self.active:
                self.active["title"] += content + " "
            if len(content) < 200:
                self.recent.append(content)
                self.recent = self.recent[-20:]

    def handle_endtag(self, tag):
        if tag == "a" and self.active is not None:
            self.active["label"] += " " + self.active["title"]
            self.matches.append(self.active)
            self.active = None


def fetch(url, *, limit=600000, extra=None):
    headers = {"User-Agent": AGENT, "Accept": "text/html,application/pdf"}
    headers.update(extra or {})
    with urlopen(Request(url, headers=headers), timeout=15) as stream:
        return stream.read(limit)


def canonical(url):
    p = urlsplit(url)
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), unquote(p.path), "", ""))


def candidate(url, label, issuer_id="1100"):
    p = urlsplit(url)
    if p.scheme != "https" or not unquote(p.path).lower().endswith(".pdf"):
        return False
    if p.hostname == "cdn.cse.lk":
        if not re.search("/upload_report_file/" + re.escape(issuer_id) + "_", unquote(p.path)):
            return False
    elif p.hostname not in ("softlogiccapital.lk", "www.softlogiccapital.lk"):
        return False
    return bool(YEAR.search(label) or YEAR.search(unquote(p.path)))


def discover(html, base, issuer_id="1100"):
    parser = Links()
    parser.feed(html)
    collected = {}
    for entry in parser.matches:
        link = urljoin(base, entry["href"])
        if candidate(link, entry["label"], issuer_id):
            collected[canonical(link)] = {"url": link, "context": entry["label"][:280], "index": base}
    for link in CSE_LINK.findall(html.replace("\\/", "/")):
        if candidate(link, link, issuer_id):
            collected.setdefault(canonical(link), {"url": link, "context": "Direct CSE PDF link", "index": base})
    return collected


def old_links():
    files = list((ROOT / "sources/records").glob("*.md")) + [ROOT / "sources/SOURCE-REGISTER.md"]
    return {canonical(url) for path in files for url in CSE_LINK.findall(path.read_text(encoding="utf-8"))}


def is_pdf(url):
    try:
        return fetch(url, limit=8, extra={"Range": "bytes=0-7", "Accept": "application/pdf"}).startswith(b"%PDF-")
    except (OSError, URLError, HTTPError, TimeoutError):
        return False


def api(method, path, token, payload=None):
    headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28", "User-Agent": AGENT}
    data = json.dumps(payload).encode() if payload is not None else None
    if data is not None:
        headers["Content-Type"] = "application/json"
    with urlopen(Request("https://api.github.com" + path, method=method, data=data, headers=headers),
                 timeout=15) as response:
        return json.load(response)


def known_issues(repo, token):
    markers = set()
    for page in range(1, 11):
        issues = api("GET", f"/repos/{repo}/issues?state=all&per_page=100&page={page}", token)
        for issue in issues:
            if "pull_request" in issue:
                continue
            markers.update(re.findall(r"SCAP_SOURCE_SHA256:([a-f0-9]{64})", issue.get("body") or ""))
        if len(issues) != 100:
            break
    return markers


def check(config, dry_run=True, token=None, repo=None):
    seen, accessible, failures = {}, 0, []
    for source in config["indexes"]:
        try:
            html = fetch(source["url"]).decode("utf-8", "replace")
            accessible += 1
            seen.update(discover(html, source["url"], config["cse_issuer_id"]))
        except (OSError, URLError, TimeoutError, HTTPError) as error:
            failures.append(source["name"] + ": " + str(error))
    for issue in failures:
        print("::warning title=Source index unavailable::" + issue.replace("%", "%25"))
    if not accessible:
        raise RuntimeError("All SCAP indexes unavailable; cannot claim nothing new")
    candidates = [data for url, data in seen.items() if url not in old_links()]
    verified = [data for data in candidates if is_pdf(data["url"])]
    print(f"Checked {accessible}/{len(config['indexes'])} indexes, found {len(seen)} PDF links, "
          f"{len(verified)} new PDF signatures; third-party catalogue entries do not count as audited reports.")
    if not verified:
        return []
    if dry_run:
        for entry in verified:
            print("DRY RUN original-file lead: " + entry["url"])
        return verified
    if not token or not repo:
        raise RuntimeError("No GitHub issue token or repository context")
    markers = known_issues(repo, token)
    for item in verified:
        digest = hashlib.sha256(canonical(item["url"]).encode()).hexdigest()
        if digest in markers:
            continue
        title = "[SCAP source discovery] " + re.sub(r"\s+", " ", item["context"])[:170]
        body = ("**Candidate original SCAP PDF with verified PDF signature.**\n\n"
                f"- PDF URL: {item['url']}\n- Index: {item['index']}\n"
                f"- Publisher context: {item['context']}\n"
                "- **Not yet an audited-source verification:** original issuer entity, audit opinion, "
                "page figures, restatements and ownership must be inspected manually.\n"
                "- [ ] Review original issuer and reporting date.\n"
                "- [ ] Create a provenance card in sources/records and index it.\n"
                "- [ ] Reconcile group/parent numbers and update translations.\n\n"
                + MARKER + digest + "\n")
        opened = api("POST", f"/repos/{repo}/issues", token, {"title": title[:240], "body": body})
        markers.add(digest)
        print("Created source-review Issue: " + opened["html_url"])
    return verified


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", type=Path, default=ROOT / "sources/watchlist.json")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    try:
        check(json.loads(args.config.read_text()), args.dry_run, os.environ.get("GH_TOKEN"),
              os.environ.get("GITHUB_REPOSITORY"))
        return 0
    except Exception as error:
        print("::error title=SCAP source monitor::" + str(error))
        return 1


if __name__ == "__main__":
    sys.exit(main())
