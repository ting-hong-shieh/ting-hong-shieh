"""Typeset text into SVG outline paths — no webfont dependency at render time."""
import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib import instancer


class Face:
    def __init__(self, path, wght=None):
        f = TTFont(path)
        if wght is not None and "fvar" in f:
            f = instancer.instantiateVariableFont(f, {"wght": wght}, updateFontNames=False)
        self.font = f
        self.upem = f["head"].unitsPerEm
        self.glyphs = f.getGlyphSet()
        self.cmap = f.getBestCmap()
        self.hmtx = f["hmtx"]

    def _gname(self, ch):
        return self.cmap.get(ord(ch))

    def width(self, text, size, tracking=0.0):
        """Advance width in px. tracking is in em units."""
        scale = size / self.upem
        w = 0.0
        for ch in text:
            g = self._gname(ch)
            if g:
                w += self.hmtx[g][0] * scale
            w += tracking * size
        return w - tracking * size if text else 0.0

    def path(self, text, size, x=0.0, y=0.0, tracking=0.0):
        """Return an SVG path 'd' string with the baseline at y, left edge at x."""
        scale = size / self.upem
        parts = []
        pen_x = x
        for ch in text:
            g = self._gname(ch)
            if g is None:
                pen_x += size * 0.3 + tracking * size
                continue
            spen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.2f}")
            tpen = TransformPen(spen, (scale, 0, 0, -scale, pen_x, y))
            self.glyphs[g].draw(tpen)
            d = spen.getCommands()
            if d:
                parts.append(d)
            pen_x += self.hmtx[g][0] * scale + tracking * size
        return " ".join(parts)

    def centered(self, text, size, cx, y, tracking=0.0):
        w = self.width(text, size, tracking)
        return self.path(text, size, cx - w / 2, y, tracking)

    def right(self, text, size, rx, y, tracking=0.0):
        w = self.width(text, size, tracking)
        return self.path(text, size, rx - w, y, tracking)


def field(x0, x1, y, height, n, seed=7, phase=0.0):
    """A deterministic hairline field — the 'procedural' motif from the site."""
    out = []
    for i in range(n):
        t = i / (n - 1)
        px = x0 + (x1 - x0) * t
        a = math.sin(t * math.pi * 6 + phase) * math.sin(t * math.pi * 2.3 + seed)
        b = math.sin(t * math.pi * 17 + seed * 1.7)
        h = height * (0.18 + 0.82 * abs(a * 0.75 + b * 0.25))
        out.append((px, y - h, h))
    return out
