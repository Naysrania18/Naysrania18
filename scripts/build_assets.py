"""Generate the profile SVG assets (light + dark). Run: python scripts/build_assets.py"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

THEMES = {
    "light": dict(bg="#ffffff", fg="#0f172a", muted="#475569", line="#e2e8f0", accent="#0f766e", panel="#f8fafc"),
    "dark": dict(bg="#0d1117", fg="#e6edf3", muted="#8b949e", line="#30363d", accent="#2dd4bf", panel="#161b22"),
}

def banner(t):
    c = THEMES[t]
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="220" stroke="{c["line"]}" stroke-width="1" opacity=".5"/>' for x in range(600, 961, 40))
    grid += "".join(f'<line x1="600" y1="{y}" x2="960" y2="{y}" stroke="{c["line"]}" stroke-width="1" opacity=".5"/>' for y in range(20, 221, 40))
    # abstract "test pipeline": nodes joined by a line, last one filled
    nodes = "".join(
        f'<circle cx="{x}" cy="110" r="9" fill="{c["accent"] if i == 4 else c["bg"]}" stroke="{c["accent"]}" stroke-width="2"/>'
        for i, x in enumerate([640, 700, 760, 820, 880])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="220" viewBox="0 0 960 220" role="img" aria-label="Sandeep Kumar Naysrania, quality and security engineer">
<rect width="960" height="220" fill="{c["bg"]}"/>
<rect x="0.5" y="0.5" width="959" height="219" fill="none" stroke="{c["line"]}"/>
{grid}
<line x1="640" y1="110" x2="880" y2="110" stroke="{c["accent"]}" stroke-width="2"/>
{nodes}
<rect x="56" y="52" width="36" height="4" fill="{c["accent"]}"/>
<text x="56" y="100" font-family="{FONT}" font-size="40" font-weight="700" fill="{c["fg"]}" letter-spacing="-0.5">Sandeep Kumar Naysrania</text>
<text x="56" y="136" font-family="{FONT}" font-size="18" fill="{c["muted"]}">Quality and security engineer</text>
<text x="56" y="162" font-family="{MONO}" font-size="13" fill="{c["accent"]}">test automation  /  API security  /  AI-assisted QA</text>
</svg>'''

COLS = [
    ("Test engineering", ["Risk-based test strategy", "API, UI, contract, SQL, ETL", "Quality gates in CI"], "pytest  Playwright  Pact  k6"),
    ("Application security", ["OWASP API Top 10 checks", "Burp Suite, ZAP, Semgrep", "SARIF reporting"], "Burp  ZAP  Semgrep  Bandit"),
    ("AI-assisted QA", ["LLM triage with validation", "MCP server, human review", "Measured precision / recall"], "Grok  Claude  MCP"),
]

def capabilities(t):
    c = THEMES[t]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="200" viewBox="0 0 960 200" role="img" aria-label="Capabilities: test engineering, application security, AI-assisted QA">',
             f'<rect width="960" height="200" fill="{c["bg"]}"/>']
    w, gap = 296, 24
    for i, (title, lines, tools) in enumerate(COLS):
        x = i * (w + gap)
        parts.append(f'<rect x="{x+.5}" y="0.5" width="{w}" height="199" rx="6" fill="{c["panel"]}" stroke="{c["line"]}"/>')
        parts.append(f'<rect x="{x}" y="0" width="{w}" height="3" fill="{c["accent"]}"/>')
        parts.append(f'<text x="{x+24}" y="42" font-family="{FONT}" font-size="17" font-weight="600" fill="{c["fg"]}">{escape(title)}</text>')
        for j, ln in enumerate(lines):
            parts.append(f'<text x="{x+24}" y="{76+j*26}" font-family="{FONT}" font-size="14" fill="{c["muted"]}">{escape(ln)}</text>')
        parts.append(f'<line x1="{x+24}" y1="160" x2="{x+w-24}" y2="160" stroke="{c["line"]}"/>')
        parts.append(f'<text x="{x+24}" y="182" font-family="{MONO}" font-size="12" fill="{c["accent"]}">{escape(tools)}</text>')
    parts.append("</svg>")
    return "\n".join(parts)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for t in THEMES:
        (OUT / f"banner-{t}.svg").write_text(banner(t), encoding="utf-8")
        (OUT / f"capabilities-{t}.svg").write_text(capabilities(t), encoding="utf-8")
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
