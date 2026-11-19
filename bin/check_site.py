#!/usr/bin/env python3
"""Validate the built academic site: local URLs, fragments, assets and CV coverage."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links = []
        self.ids = set()
        self.text = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src", "poster"):
            if attrs.get(key):
                self.links.append(attrs[key])

    def handle_data(self, data):
        self.text.append(data)


def main():
    errors = []
    pages = {path: Document(path) for path in SITE.rglob("*.html")}
    assert pages, "Build the site first: bundle exec jekyll build"
    checked = 0
    for path, document in pages.items():
        current = "/" + path.relative_to(SITE).as_posix()
        for href in document.links:
            url = urlsplit(urljoin(current, href))
            if url.scheme or url.netloc:
                continue
            target = SITE / unquote(url.path).lstrip("/")
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{current}: missing {href}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{current}: missing fragment {href}")
            checked += 1
    for route in ("index.html", "research/index.html", "publications/index.html", "cv/index.html", "teaching/index.html", "beyond/index.html"):
        assert SITE / route in pages, f"Missing route: {route}"
    cv = yaml.safe_load((ROOT / "_data/cv.yml").read_text())["cv"]
    cv_text = " ".join(pages[SITE / "cv/index.html"].text)
    for heading in cv["sections"]:
        assert heading in cv_text, f"CV section missing: {heading}"
    for section in cv["sections"].values():
        for entry in section:
            if isinstance(entry, dict):
                for key in ("title", "summary", "details"):
                    if entry.get(key):
                        assert entry[key] in cv_text, f"CV field missing: {entry[key]}"
    for page in pages.values():
        text = " ".join(page.text)
        assert "Albert Einstein" not in text, "Template biography leaked into the site"
    for asset in ("assets/css/main.css", "assets/css/tailwind.css", "assets/css/academic.css", "assets/img/prof_pic.png", "assets/rendercv/rendercv_output/Fatemah_Alhamdoosh_CV.pdf"):
        assert (SITE / asset).stat().st_size > 0, f"Missing or empty asset: {asset}"
    pdf = SITE / "assets/rendercv/rendercv_output/Fatemah_Alhamdoosh_CV.pdf"
    assert pdf.read_bytes().startswith(b"%PDF-"), "Download is not a PDF"
    config = yaml.safe_load((ROOT / "_config.yml").read_text())
    assert config["url"] == "https://fatemah-alh.github.io" and config["baseurl"] == ""
    assert not errors, "\n".join(errors)
    print(f"Passed: {len(pages)} HTML pages, {checked} local references, all CV sections and required assets.")


if __name__ == "__main__":
    main()
