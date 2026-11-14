"""Generate the dark cyber-tech profile assets. Run: python scripts/build_cyber_assets.py"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Courier New',monospace"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
CY, TEAL, TXT, MUTED = "#00e5ff", "#14f1d9", "#e6edf3", "#8b949e"

DEFS = f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a0f1a"/><stop offset="1" stop-color="#0d1117"/></linearGradient>
<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset=".5" stop-color="{CY}"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></linearGradient>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>'''


def banner():
    traces = [
        ("M0 60 H140 L170 90 H330", (330, 90)), ("M0 270 H90 L120 255 H260", (260, 255)),
        ("M1200 40 H1060 L1030 70 H900", (900, 70)), ("M1200 260 H1100 L1070 230 H950", (950, 230)),
        ("M520 0 V40 L550 70 H700", (700, 70)), ("M640 300 V262 L610 232 H500", (500, 232)),
    ]
    paths = "".join(f'<path d="{d}" fill="none" stroke="{CY}" stroke-opacity=".35" stroke-width="1.2"/>' for d, _ in traces)
    nodes = "".join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#0a0f1a" stroke="{TEAL}" stroke-width="1.5" filter="url(#glow)"/>' for _, (x, y) in traces)
    icon = f'''<g transform="translate(1062 108)" filter="url(#glow)" fill="none" stroke="{CY}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">
<path d="M40 4 L76 18 V50 C76 74 60 90 40 98 C20 90 4 74 4 50 V18 Z"/><path d="M24 50 L36 62 L58 38"/></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Sandeep Kumar Naysrania, quality and security engineer">
{DEFS}
<rect width="1200" height="300" fill="url(#bg)"/>
{paths}{nodes}
<rect x="1.5" y="1.5" width="1197" height="297" fill="none" stroke="{CY}" stroke-opacity=".45" stroke-width="1.5"/>
<text x="64" y="160" font-family="{SANS}" font-size="46" font-weight="700" fill="{TXT}" letter-spacing="-0.5">Sandeep Kumar Naysrania</text>
<rect x="64" y="182" width="56" height="3" fill="{CY}" filter="url(#glow)"/>
<text x="64" y="218" font-family="{MONO}" font-size="14" fill="{MUTED}">test automation / API security / AI-assisted QA</text>
<text x="1030" y="150" text-anchor="end" font-family="{MONO}" font-size="34" font-weight="700" fill="{CY}" filter="url(#glow)">QUALITY &amp;</text>
<text x="1030" y="192" text-anchor="end" font-family="{MONO}" font-size="34" font-weight="700" fill="{CY}" filter="url(#glow)">SECURITY ENGINEER</text>
{icon}
</svg>'''


STATS = [("210+", "Python tests", "issue-tracker-quality-lab"),
         ("66", "Java tests", "issue-tracker-quality-lab"),
         ("20+", "Security labs documented", "BSCP-2026")]


def stats():
    w, gap, parts = 376, 36, []
    for i, (n, label, src) in enumerate(STATS):
        x = 6 + i * (w + gap)
        parts.append(f'''<g transform="translate({x} 6)">
<rect width="{w}" height="138" rx="14" fill="#0a0f1a" stroke="{CY}" stroke-width="1.5" filter="url(#glow)"/>
<text x="{w/2}" y="68" text-anchor="middle" font-family="{SANS}" font-size="50" font-weight="700" fill="{CY}" filter="url(#glow)">{n}</text>
<text x="{w/2}" y="98" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{TXT}">{label}</text>
<text x="{w/2}" y="120" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{MUTED}">{src}</text></g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="150" viewBox="0 0 1200 150" role="img" aria-label="Test and lab counts">
{DEFS}{"".join(parts)}</svg>'''


def divider():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="16" viewBox="0 0 1200 16" role="img" aria-label="">
{DEFS}
<line x1="0" y1="8" x2="1200" y2="8" stroke="url(#ln)" stroke-width="1.5"/>
<circle r="3.5" cy="8" fill="{CY}" filter="url(#glow)"><animate attributeName="cx" from="0" to="1200" dur="6s" repeatCount="indefinite"/></circle>
</svg>'''


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    import build_process_assets as bp
    for name, fn in (("banner", banner), ("stats", stats), ("divider", divider), ("pipeline", bp.pipeline), ("stack", bp.stack)):
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
    print("wrote banner, stats, divider, pipeline, stack")
