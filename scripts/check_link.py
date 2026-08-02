#!/usr/bin/env python3
"""Verify an exchange backlink on a published page. Standard library only.

Usage:
  python check_link.py <published_url> <partner_domain> [--json]

Checks:
  - the link exists and points at partner_domain
  - rel attribute (nofollow / sponsored / ugc disqualify it)
  - placement: body content vs footer / nav / sidebar / header
  - anchor text
  - host post word count
  - total outbound links on the page
  - how many OTHER exchange-style outbound links sit in the same post
"""
import sys, json, re
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen

UA = "Mozilla/5.0 (compatible; BacklinkExchangeChecker/1.0)"
NON_BODY = {"footer", "nav", "aside", "header"}
SKIP_TEXT = {"script", "style", "noscript", "template"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.links = []          # dicts
        self.words = 0
        self._cur = None         # open <a> being captured

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        if tag == "a":
            d = dict(attrs)
            href = (d.get("href") or "").strip()
            self._cur = {
                "href": href,
                "rel": (d.get("rel") or "").lower(),
                "anchor": "",
                "in_non_body": any(t in NON_BODY for t in self.stack),
                "in_article": any(t in ("article", "main") for t in self.stack),
            }

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag == "a" and self._cur is not None:
            self._cur["anchor"] = " ".join(self._cur["anchor"].split())
            self.links.append(self._cur)
            self._cur = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if any(t in SKIP_TEXT for t in self.stack):
            return
        if self._cur is not None:
            self._cur["anchor"] += data
        if not any(t in NON_BODY for t in self.stack):
            self.words += len(data.split())


def norm(domain):
    d = domain.lower().strip()
    d = re.sub(r"^https?://", "", d).split("/")[0]
    return d[4:] if d.startswith("www.") else d


def fetch(url):
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as r:
        raw = r.read()
    for enc in ("utf-8", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def check(published_url, partner_domain):
    target = norm(partner_domain)
    host = norm(urlparse(published_url).netloc)
    html = fetch(published_url)
    p = PageParser()
    p.feed(html)

    matches, outbound, other_ext = [], 0, set()
    for l in p.links:
        href = l["href"]
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        absolute = urljoin(published_url, href)
        h = norm(urlparse(absolute).netloc)
        if not h or h == host:
            continue
        outbound += 1
        other_ext.add(h)
        if h == target or h.endswith("." + target):
            l["resolved"] = absolute
            matches.append(l)

    bad_rel = ("nofollow", "sponsored", "ugc")
    result = {
        "published_url": published_url,
        "partner_domain": target,
        "found": bool(matches),
        "count_to_partner": len(matches),
        "word_count": p.words,
        "total_outbound_links": outbound,
        "distinct_external_domains": len(other_ext),
        "links": [],
        "checks": {},
        "verdict": "FAIL",
        "reasons": [],
    }

    if not matches:
        result["reasons"].append("No link to the partner domain found on this page.")
        return result

    best = None
    for m in matches:
        rec = {
            "href": m["resolved"],
            "anchor": m["anchor"] or "(no anchor text)",
            "rel": m["rel"] or "(none)",
            "dofollow": not any(b in m["rel"] for b in bad_rel),
            "in_body": not m["in_non_body"],
            "in_article_or_main": m["in_article"],
        }
        result["links"].append(rec)
        if best is None or (rec["dofollow"] and rec["in_body"]):
            best = rec

    c = result["checks"]
    c["link_present"] = True
    c["dofollow"] = best["dofollow"]
    c["in_body_content"] = best["in_body"]
    c["single_link_to_partner"] = len(matches) == 1
    c["word_count_600_plus"] = p.words >= 600
    c["outbound_under_15"] = outbound <= 15
    c["anchor_not_empty"] = bool(best["anchor"].strip())

    if not c["dofollow"]:
        result["reasons"].append("Link is nofollow/sponsored/ugc. It must be a plain dofollow link.")
    if not c["in_body_content"]:
        result["reasons"].append("Link sits in a footer, nav, header or sidebar. Move it into a body paragraph.")
    if not c["single_link_to_partner"]:
        result["reasons"].append(f"{len(matches)} links point at the partner. Exactly one per post.")
    if not c["word_count_600_plus"]:
        result["reasons"].append(f"Post is {p.words} words. Minimum is 600.")
    if not c["outbound_under_15"]:
        result["reasons"].append(f"{outbound} outbound links on this page. Keep it under 15.")
    if not c["anchor_not_empty"]:
        result["reasons"].append("Link has no anchor text (image or empty link).")

    result["verdict"] = "PASS" if all(c.values()) else "FAIL"
    return result


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    as_json = "--json" in sys.argv
    if len(args) < 2:
        print("usage: check_link.py <published_url> <partner_domain> [--json]")
        sys.exit(2)
    try:
        r = check(args[0], args[1])
    except Exception as e:
        r = {"verdict": "ERROR", "error": str(e), "published_url": args[0]}
    if as_json:
        print(json.dumps(r, indent=2))
        return
    print(f"\n  {r['verdict']}  {r.get('published_url','')}")
    if r["verdict"] == "ERROR":
        print(f"  Could not fetch: {r['error']}")
        return
    for k, v in r.get("checks", {}).items():
        print(f"    {'PASS' if v else 'FAIL'}  {k}")
    if r.get("links"):
        l = r["links"][0]
        print(f"\n  anchor: {l['anchor']}\n  rel:    {l['rel']}\n  href:   {l['href']}")
    print(f"\n  words: {r.get('word_count')}   outbound links: {r.get('total_outbound_links')}")
    for reason in r.get("reasons", []):
        print(f"  - {reason}")
    print()


if __name__ == "__main__":
    main()
