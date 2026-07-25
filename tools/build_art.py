"""Generate the profile README's typographic plates.

    python3 -m venv venv && ./venv/bin/pip install fonttools
    ./venv/bin/python tools/build_art.py

Fonts are fetched on first run into tools/fonts/ (gitignored). Both are
SIL Open Font License 1.1 — the same pair eliasshieh.com uses, so the README
and the site stay one typographic voice.

Text is converted to outlines rather than set as <text>. GitHub proxies README
images through camo and renders them detached from any webfont, so a live font
reference would silently fall back to a system face.
"""
import os
import urllib.request

from typeset import Face, field

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, os.pardir, "art")

FONTS = {
    "SpaceGrotesk.ttf":
        "https://github.com/google/fonts/raw/main/ofl/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf",
    "IBMPlexMono-Regular.ttf":
        "https://github.com/google/fonts/raw/main/ofl/ibmplexmono/IBMPlexMono-Regular.ttf",
}


def font(name):
    os.makedirs(FONT_DIR, exist_ok=True)
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        print(f"fetching {name}")
        urllib.request.urlretrieve(FONTS[name], path)
    return path


light = Face(font("SpaceGrotesk.ttf"), wght=300)
med = Face(font("SpaceGrotesk.ttf"), wght=500)
mono = Face(font("IBMPlexMono-Regular.ttf"))

# Ink per GitHub theme. Two files per plate, switched by a <picture> media query.
THEMES = {"dark": "#EDEDED", "light": "#141414"}

WORDMARK = "ELIAS SHIEH"
TAGLINE = "I TURN COMPLEX IDEAS INTO WORKING INSTRUMENTS"
PLACE = "TAIPEI · 25.03°N 121.57°E"
COLOPHON = "ELIAS SHIEH · NO STRAIGHT LINE · MMXXVI"

# Justified across the masthead's bottom rule. Keep every claim checkable:
# the IQC rank is the Taiwan field, not the global one.
RAIL = [
    "MCS · UIUC",
    "IQC · 1ST OF 373 TW",
    "EVERRIST · B2B",
    "IPHO COACH · 3 MEDALS",
    "B.SC. EE · NTU",
]

LABELS = [
    ("label-work", "SELECTED WORK", "01"),
    ("label-tools", "INSTRUMENTS", "02"),
    ("label-elsewhere", "ELSEWHERE", "03"),
]

W = 1200   # design width; the README scales it down to the container
M = 28     # margin, tuned so the rules sit flush with the body text column


def svg(h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" '
            f'width="{W}" height="{h}" role="img">\n{body}\n</svg>\n')


def rule(y, ink, op=0.28):
    return f'<rect x="{M}" y="{y}" width="{W - 2 * M}" height="1" fill="{ink}" opacity="{op}"/>'


def p(d, ink, op=1.0):
    return f'<path d="{d}" fill="{ink}" opacity="{op}"/>'


def bars(items, ink, op=0.30, dur=7.0):
    """The hairline field, breathing. SMIL animates even inside <img>."""
    out = []
    for i, (x, y, h) in enumerate(items):
        out.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="0.9" height="{h:.2f}" fill="{ink}" opacity="{op}">'
            f'<animate attributeName="opacity" values="{op};{op * 2.4:.2f};{op * 0.45:.2f};{op}" '
            f'dur="{dur}s" begin="{-dur * (i / len(items)) * 2.0:.2f}s" repeatCount="indefinite" '
            f'calcMode="spline" keyTimes="0;0.35;0.7;1" '
            f'keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1"/></rect>')
    return "\n".join(out)


def masthead(ink):
    b = [rule(54, ink),
         p(mono.path("ELIASSHIEH.COM", 13, M, 40, tracking=0.14), ink, 0.55),
         p(mono.centered("Nº 01", 13, W / 2, 40, tracking=0.14), ink, 0.55),
         p(mono.right(PLACE, 13, W - M, 40, tracking=0.14), ink, 0.55),
         p(light.centered(WORDMARK, 104, W / 2, 208, tracking=0.14), ink),
         bars(field(M, W - M, 268, 34, 150), ink, 0.30),
         p(med.centered(TAGLINE, 19, W / 2, 330, tracking=0.30), ink, 0.92),
         rule(372, ink)]

    widths = [mono.width(t, 13, 0.14) for t in RAIL]
    gap = (W - 2 * M - sum(widths)) / (len(RAIL) - 1)
    x = M
    for t, w in zip(RAIL, widths):
        b.append(p(mono.path(t, 13, x, 404, tracking=0.14), ink, 0.55))
        x += w + gap
    return svg(460, "\n".join(b))


def signoff(ink):
    b = [rule(30, ink, 0.18),
         bars(field(M, W - M, 92, 26, 150, seed=3, phase=1.4), ink, 0.22, dur=9.0),
         p(mono.centered(COLOPHON, 13, W / 2, 126, tracking=0.28), ink, 0.6)]
    return svg(150, "\n".join(b))


def label(text, num):
    def make(ink):
        b = [p(mono.path(num, 12, M, 26, tracking=0.14), ink, 0.40),
             p(med.path(text, 15, M + 46, 26, tracking=0.30), ink, 0.90),
             rule(44, ink, 0.20)]
        return svg(62, "\n".join(b))
    return make


PLATES = [("masthead", masthead), ("signoff", signoff)]
PLATES += [(name, label(text, num)) for name, text, num in LABELS]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in PLATES:
        for theme, ink in THEMES.items():
            path = os.path.join(OUT, f"{name}-{theme}.svg")
            with open(path, "w") as f:
                f.write(fn(ink))
            print(f"art/{name}-{theme}.svg  {os.path.getsize(path) / 1024:.1f} KB")
