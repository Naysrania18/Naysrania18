"""Generate the dark cyber-tech profile assets. Run: python scripts/build_cyber_assets.py"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
MONO = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
CY, TEAL, TXT, MUTED = "#00e5ff", "#14f1d9", "#e6edf3", "#8b949e"

DEFS = f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a0f1a"/><stop offset="1" stop-color="#0d1117"/></linearGradient>
<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset=".5" stop-color="{CY}"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></linearGradient>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>'''


def banner(cal=None):
    from textpath import text_path
    NAME_D = text_path("sg-700.woff", "Sandeep Kumar Naysrania", 46, 64, 150, spacing=-0.4)
    SUB_D = text_path("inter-400.woff", "Test automation   |   API security   |   AI-assisted QA", 16, 64, 208)
    """Name + role on the left; compact contribution heatmap (last 26 weeks) on the right."""
    traces = [("M0 60 H140 L170 90 H330", (330, 90)), ("M0 270 H90 L120 255 H260", (260, 255)),
              ("M1200 40 H1100 L1070 64 H960", (960, 64)), ("M1200 262 H1100 L1070 238 H960", (960, 238))]
    paths = "".join(f'<path d="{d}" fill="none" stroke="{CY}" stroke-opacity=".22" stroke-width="1.2"/>' for d, _ in traces)
    nodes = "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#0a0f1a" stroke="{TEAL}" stroke-width="1.5"/>' for _, (x, y) in traces)
    heat = ""
    if cal:
        weeks = cal["weeks"][-26:]
        import datetime
        mx = max((d["contributionCount"] for w in weeks for d in w["contributionDays"]), default=1) or 1
        op = lambda n: 0.08 if n == 0 else 0.3 if n / mx <= .25 else 0.55 if n / mx <= .5 else 0.8 if n / mx <= .75 else 1.0
        cell, gap, x0, y0 = 12, 3, 790, 104
        def cell_svg(i, d):
            n = d["contributionCount"]; o = op(n); peak = min(o + 0.55, 1.0)
            x = x0 + i * (cell + gap); y = y0 + datetime.date.fromisoformat(d["date"]).weekday() * (cell + gap)
            return (f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2.5" fill="{CY}" fill-opacity="{o}">'
                    f'<animate attributeName="fill-opacity" values="{o};{peak};{o}" keyTimes="0;0.5;1" dur="3.6s" begin="{i*0.09:.2f}s" repeatCount="indefinite"/></rect>')
        cells = "".join(cell_svg(i, d) for i, w in enumerate(weeks) for d in w["contributionDays"])
        total = sum(d["contributionCount"] for w in weeks for d in w["contributionDays"])
        heat = (f'<text x="{x0}" y="{y0-16}" font-family="{SANS}" font-size="13" font-weight="600" fill="{TXT}">{total} contributions <tspan fill="{MUTED}" font-weight="400">in the last 6 months</tspan></text>' + cells)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Sandeep Kumar Naysrania, quality and security engineer, with a contribution graph">
{DEFS}
<rect width="1200" height="300" fill="url(#bg)"/>
{paths}{nodes}
<rect x="1.5" y="1.5" width="1197" height="297" fill="none" stroke="{CY}" stroke-opacity=".4" stroke-width="1.5"/>
<path d="{NAME_D}" fill="{TXT}"/>
<rect x="64" y="172" width="56" height="3" fill="{CY}"/>
<path d="{SUB_D}" fill="{MUTED}"/>
{heat}
</svg>'''


def tagline():
    from textpath import text_path, width
    t1, t2 = "Quality and security engineering, ", "automated."
    size = 26; w1 = width("sg-500.woff", t1, size); w2 = width("sg-500.woff", t2, size)
    x = 600 - (w1 + w2) / 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="64" viewBox="0 0 1200 64" role="img" aria-label="Quality and security engineering, automated.">
{DEFS}
<rect width="1200" height="64" rx="12" fill="url(#bg)" stroke="{CY}" stroke-opacity=".3"/>
<path d="{text_path("sg-500.woff", t1, size, x, 40)}" fill="{TXT}"/>
<path d="{text_path("sg-500.woff", t2, size, x + w1, 40)}" fill="{CY}"/>
</svg>'''


def linkedin():
    import json
    ic = json.loads((Path(__file__).parent / "icons.json").read_text())["linkedin"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="44" viewBox="0 0 220 44" role="img" aria-label="LinkedIn: sandeepnaysrania">
{DEFS}
<rect x="1" y="1" width="218" height="42" rx="10" fill="#0a0f1a" stroke="{CY}" stroke-opacity=".6" stroke-width="1.4"/>
<g transform="translate(14 10)"><path d="{ic["d"]}" fill="#0A66C2"/></g>
<text x="50" y="27" font-family="{SANS}" font-size="15" font-weight="600" fill="{TXT}">LinkedIn</text>
<text x="118" y="27" font-family="{SANS}" font-size="12" fill="{MUTED}">sandeepnaysrania</text>
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
    import build_process_assets as bp
    import build_activity as ba
    cal = ba.fetch("Naysrania18")["contributionsCollection"]["contributionCalendar"]
    OUT.mkdir(exist_ok=True)
    jobs = (("banner", lambda: banner(cal)), ("stats", stats), ("pipeline", bp.pipeline), ("stack", bp.stack), ("linkedin", linkedin), ("tagline", tagline))
    for name, fn in jobs:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
    print("wrote banner, stats, pipeline, stack, linkedin, tagline")
