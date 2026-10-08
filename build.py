#!/usr/bin/env python3
"""Static site generator for CESA. Renders content.py + templates/*
into standalone HTML files at the repo root (ready for GitHub Pages)."""
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(ROOT, "templates")

env = Environment(
    loader=FileSystemLoader(TEMPLATES),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


def build():
    count = 0
    for page in C.PAGES:
        tpl = env.get_template(f"{page['template']}.html")
        ctx = {
            "base": "",
            "site": C.SITE,
            "nav": C.NAV,
            "title": page["title"],
            "description": page.get("description", ""),
            "hero": page.get("hero"),
            "sections": page.get("sections", []),
            "pillars": page.get("pillars"),
            "cat_nav": page.get("cat_nav"),
            "solid_header": page["template"] != "home",
            "og_url": C.SITE_URL + page["slug"],
            "og_image": C.SITE_URL + "assets/img/brand/og-image.jpg",
        }
        html = tpl.render(**ctx)
        out_path = os.path.join(ROOT, page["slug"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
    print(f"Built {count} pages.")


if __name__ == "__main__":
    build()
