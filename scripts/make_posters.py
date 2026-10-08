#!/usr/bin/env python3
"""Generates branded SVG illustrations for CESA (no stock photography available yet).
Consistent visual language: navy->teal gradient, faint blueprint/circuit grid,
amber line-art glyph(s). Run from repo root: python3 scripts/make_posters.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAVY_DARK = "#0a140d"
NAVY = "#16281c"
NAVY_LIGHT = "#27432f"
AMBER = "#3fc456"
AMBER_LIGHT = "#8de39a"
WHITE = "#ffffff"

# Inner glyph paths, viewBox 0 0 24 24, stroke-based (matches templates/_icons.html)
GLYPHS = {
    "sun": '<circle cx="12" cy="12" r="4.5"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
    "bolt": '<path d="M13 2L4 14h6l-1 8 9-12h-6l1-8z"/>',
    "snow": '<path d="M12 2v20M4.5 6l15 12M19.5 6l-15 12"/><path d="M8 3.5L12 6l4-2.5M8 20.5L12 18l4 2.5M3 9l3 3-3 3M21 9l-3 3 3 3"/>',
    "elevator": '<rect x="4" y="2" width="16" height="20" rx="1.5"/><path d="M9 8l3-3 3 3M9 16l3 3 3-3"/>',
    "flame": '<path d="M12 22a6.5 6.5 0 0 0 6.5-6.5c0-3.2-2.1-4.7-2.8-6.6-.3 1.1-.2 2.1-1.1 2.8.3-2.6-1-4-2.1-5.9-.7 1.8-2.1 2.8-2.1 5.1 0 1-.4 1.6-1 1.9-.4-1-.2-1.9.1-2.8C7.6 11.3 5.5 13 5.5 15.5A6.5 6.5 0 0 0 12 22z"/>',
    "shield": '<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>',
    "network": '<circle cx="12" cy="4" r="2"/><circle cx="5" cy="20" r="2"/><circle cx="19" cy="20" r="2"/><path d="M12 6v5M12 11L6.5 18M12 11L17.5 18"/>',
    "crane": '<path d="M4 21V9l9-6 2 2-9 6v10"/><path d="M13 5l8 2-3 3M4 21h16M9 21v-6h4v6"/>',
    "building": '<path d="M3 21V7l8-4 8 4v14"/><path d="M3 21h18M9 9h.01M9 13h.01M15 9h.01M15 13h.01M9 21v-4h6v4"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M8.5 13.5L7 22l5-3 5 3-1.5-8.5"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .34 1.87l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.7 1.7 0 0 0-1.87-.34 1.7 1.7 0 0 0-1 1.55V21a2 2 0 0 1-4 0v-.09A1.7 1.7 0 0 0 9 19.36a1.7 1.7 0 0 0-1.87.34l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.7 1.7 0 0 0 4.64 15a1.7 1.7 0 0 0-1.55-1H3a2 2 0 0 1 0-4h.09A1.7 1.7 0 0 0 4.64 9a1.7 1.7 0 0 0-.34-1.87l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.7 1.7 0 0 0 9 4.64a1.7 1.7 0 0 0 1-1.55V3a2 2 0 0 1 4 0v.09a1.7 1.7 0 0 0 1 1.55 1.7 1.7 0 0 0 1.87-.34l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.7 1.7 0 0 0 19.36 9c.27.61.85 1 1.55 1H21a2 2 0 0 1 0 4h-.09a1.7 1.7 0 0 0-1.51 1z"/>',
    "pin": '<path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "plane": '<path d="M3 13l18-8-6 18-3-7-6-3z"/>',
    "drop": '<path d="M12 2.5s7 7.4 7 12.5a7 7 0 0 1-14 0c0-5.1 7-12.5 7-12.5z"/>',
    "wave": '<path d="M3 12h2M8 7v10M13 4v16M18 7v10M22 12h-1"/>',
}


def glyph(name, x, y, size, color=AMBER, opacity=1, stroke_width=1.3):
    inner = GLYPHS[name]
    scale = size / 24
    return (
        f'<g transform="translate({x - size/2},{y - size/2}) scale({scale})" '
        f'fill="none" stroke="{color}" stroke-width="{stroke_width/scale:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}">{inner}</g>'
    )


def blueprint_grid(w, h, step=48, color=WHITE, opacity=0.05):
    lines = []
    x = 0
    while x <= w:
        lines.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>')
        x += step
    y = 0
    while y <= h:
        lines.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>')
        y += step
    return f'<g stroke="{color}" stroke-width="1" opacity="{opacity}">{"".join(lines)}</g>'


def card(w, h, glyphs, grid_step=40, radial=True, filename=None, corner_icon=None):
    gid = f"g{abs(hash(filename)) % 100000}" if filename else "g0"
    stops = f"""
      <linearGradient id="{gid}-bg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="{NAVY_LIGHT}"/>
        <stop offset="55%" stop-color="{NAVY}"/>
        <stop offset="100%" stop-color="{NAVY_DARK}"/>
      </linearGradient>
      <radialGradient id="{gid}-glow" cx="78%" cy="18%" r="60%">
        <stop offset="0%" stop-color="{AMBER}" stop-opacity="0.35"/>
        <stop offset="100%" stop-color="{AMBER}" stop-opacity="0"/>
      </radialGradient>
    """
    glow = f'<rect width="{w}" height="{h}" fill="url(#{gid}-glow)"/>' if radial else ""
    glyph_markup = "".join(glyphs)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>{stops}</defs>
  <rect width="{w}" height="{h}" fill="url(#{gid}-bg)"/>
  {blueprint_grid(w, h, step=grid_step)}
  {glow}
  {glyph_markup}
  <rect width="{w}" height="{h}" fill="none" stroke="{AMBER}" stroke-opacity="0.18" stroke-width="2"/>
</svg>'''
    return svg


def write(path, svg):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", path)


# ---------------------------------------------------------------- HERO (1600x820)
HW, HH = 1600, 820

hero_defs = {
    "hero/home-1.svg": [glyph("bolt", HW*0.78, HH*0.30, 230, opacity=.5), glyph("sun", HW*0.20, HH*0.70, 170, opacity=.35)],
    "hero/home-2.svg": [glyph("sun", HW*0.75, HH*0.35, 240, opacity=.5), glyph("drop", HW*0.18, HH*0.65, 150, opacity=.3)],
    "hero/home-3.svg": [glyph("shield", HW*0.76, HH*0.32, 220, opacity=.5), glyph("network", HW*0.20, HH*0.68, 170, opacity=.32)],
    "hero/a-propos.svg": [glyph("building", HW*0.78, HH*0.5, 260, opacity=.45), glyph("award", HW*0.18, HH*0.3, 140, opacity=.3)],
    "hero/expertises.svg": [glyph("gear", HW*0.78, HH*0.5, 260, opacity=.4), glyph("bolt", HW*0.16, HH*0.3, 130, opacity=.3), glyph("sun", HW*0.20, HH*0.72, 120, opacity=.25)],
    "hero/realisations.svg": [glyph("crane", HW*0.78, HH*0.5, 260, opacity=.45), glyph("award", HW*0.18, HH*0.28, 140, opacity=.3)],
    "hero/references.svg": [glyph("award", HW*0.78, HH*0.5, 250, opacity=.45), glyph("building", HW*0.18, HH*0.3, 150, opacity=.3)],
    "hero/contact.svg": [glyph("pin", HW*0.78, HH*0.5, 250, opacity=.45), glyph("network", HW*0.18, HH*0.3, 140, opacity=.3)],
}
for path, glyphs in hero_defs.items():
    write(f"assets/img/{path}", card(HW, HH, glyphs, filename=path))

# ---------------------------------------------------------------- CATEGORY CARDS (900x680)
CW, CH = 900, 680
categories = {
    "expertises/energie.svg": ["sun", "bolt"],
    "expertises/electricite.svg": ["bolt", "gear"],
    "expertises/climatisation.svg": ["snow"],
    "expertises/sanitaire.svg": ["drop"],
    "expertises/acoustique.svg": ["wave"],
    "expertises/securite.svg": ["flame", "shield"],
    "expertises/ascenseurs.svg": ["elevator"],
    "expertises/communication.svg": ["network"],
    "expertises/genie-civil.svg": ["crane"],
}
for path, names in categories.items():
    glyphs = []
    if len(names) == 1:
        glyphs.append(glyph(names[0], CW*0.68, CH*0.46, 260, opacity=.75))
    else:
        glyphs.append(glyph(names[0], CW*0.62, CH*0.42, 230, opacity=.8))
        glyphs.append(glyph(names[1], CW*0.80, CH*0.68, 140, opacity=.45))
    write(f"assets/img/{path}", card(CW, CH, glyphs, grid_step=36, filename=path))

# ---------------------------------------------------------------- REALISATIONS POSTERS (1000x760)
RW, RH = 1000, 760
projects = {
    "realisations/aeroport-cadjehoun.svg": ["plane", "building"],
    "realisations/presidence.svg": ["building", "shield"],
    "realisations/eclairage-routier.svg": ["bolt", "sun"],
    "realisations/solaire-industriel.svg": ["sun", "gear"],
    "realisations/climatisation-tertiaire.svg": ["snow", "building"],
    "realisations/protection-incendie.svg": ["flame", "shield"],
}
for path, names in projects.items():
    glyphs = [
        glyph(names[0], RW*0.64, RH*0.44, 280, opacity=.8),
        glyph(names[1], RW*0.82, RH*0.70, 150, opacity=.4),
    ]
    write(f"assets/img/{path}", card(RW, RH, glyphs, grid_step=40, filename=path))

print("Done.")
