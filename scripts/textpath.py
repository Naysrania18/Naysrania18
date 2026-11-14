"""Convert text to SVG path data using an embedded open-licence font, so GitHub renders it with that font."""
from functools import lru_cache
from pathlib import Path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS = Path(__file__).parent / "fonts"


@lru_cache(maxsize=None)
def _font(name):
    return TTFont(FONTS / name)


def width(font, text, size, spacing=0.0):
    f = _font(font); upm = f["head"].unitsPerEm; cmap = f.getBestCmap(); hm = f["hmtx"]
    return sum(hm[cmap[ord(c)]][0] * size / upm + spacing for c in text if ord(c) in cmap)


def text_path(font, text, size, x, y, spacing=0.0, anchor="start"):
    """Return one SVG path 'd' string for `text` with the baseline at y."""
    f = _font(font); upm = f["head"].unitsPerEm; cmap = f.getBestCmap(); gs = f.getGlyphSet(); hm = f["hmtx"]
    s = size / upm
    if anchor == "middle":
        x -= width(font, text, size, spacing) / 2
    elif anchor == "end":
        x -= width(font, text, size, spacing)
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}")
    cx = x
    for ch in text:
        g = cmap.get(ord(ch))
        if g is None:
            continue
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        cx += hm[g][0] * s + spacing
    return pen.getCommands()
