"""Process animation (application + security testing) and tech stack SVGs."""
import json
from pathlib import Path
from build_cyber_assets import DEFS, MONO, SANS, CY, TEAL, TXT, MUTED

ICONS = json.loads((Path(__file__).parent / "icons.json").read_text())
CYCLE = 10.0  # seconds

APP = ["Requirements", "Unit + API", "Contract + UI", "Performance"]
SEC = ["Threat model", "SAST triage", "API checks", "DAST scan"]
XS = [150, 400, 650, 900]
Y_APP, Y_SEC, GATE = 95, 215, (1085, 155)


def _lit(i, n=4):
    """keyTimes/values so stage i pulses as the packet passes it."""
    c = (XS[i] - 60) / (GATE[0] - 60) * 0.8  # packet travels in first 80% of cycle
    a, b, e = max(c - 0.03, 0.001), c + 0.04, c + 0.12
    return f'keyTimes="0;{a:.3f};{b:.3f};{e:.3f};1" values="0.25;0.25;1;0.25;0.25"'


def _stage(x, y, label, i, tag):
    return f'''<g>
<rect x="{x-86}" y="{y-26}" width="172" height="52" rx="10" fill="#0a0f1a" stroke="{CY}" stroke-width="1.6" stroke-opacity="0.25">
<animate attributeName="stroke-opacity" {_lit(i)} dur="{CYCLE}s" repeatCount="indefinite"/></rect>
<text x="{x}" y="{y-3}" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="600" fill="{TXT}">{label}</text>
<text x="{x}" y="{y+15}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{MUTED}">{tag}</text></g>'''


def pipeline():
    app_tags = ["scope + risk", "pytest, TestNG", "Pact, Playwright", "load tests"]
    sec_tags = ["assets + abuse cases", "static analysis", "BOLA, auth, injection", "OWASP ZAP"]
    lanes = f'''<path id="la" d="M60 {Y_APP} H{GATE[0]-60} L{GATE[0]} {GATE[1]}" fill="none" stroke="{CY}" stroke-opacity=".35" stroke-width="1.5"/>
<path id="ls" d="M60 {Y_SEC} H{GATE[0]-60} L{GATE[0]} {GATE[1]}" fill="none" stroke="{TEAL}" stroke-opacity=".35" stroke-width="1.5"/>'''
    stages = "".join(_stage(x, Y_APP, l, i, t) for i, (x, l, t) in enumerate(zip(XS, APP, app_tags)))
    stages += "".join(_stage(x, Y_SEC, l, i, t) for i, (x, l, t) in enumerate(zip(XS, SEC, sec_tags)))
    pkt = lambda ref, col: f'''<circle r="5" fill="{col}" filter="url(#glow)"><animateMotion dur="{CYCLE}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;0.8;1" calcMode="linear"><mpath href="#{ref}"/></animateMotion></circle>'''
    gate = f'''<g>
<circle cx="{GATE[0]+10}" cy="{GATE[1]}" r="34" fill="#0a0f1a" stroke="{TEAL}" stroke-width="2" filter="url(#glow)">
<animate attributeName="stroke-opacity" keyTimes="0;0.78;0.85;0.97;1" values="0.3;0.3;1;1;0.3" dur="{CYCLE}s" repeatCount="indefinite"/></circle>
<path d="M{GATE[0]-4} {GATE[1]+1} l10 10 l20 -22" fill="none" stroke="{TEAL}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
<animate attributeName="opacity" keyTimes="0;0.82;0.88;0.97;1" values="0;0;1;1;0" dur="{CYCLE}s" repeatCount="indefinite"/></path>
<text x="{GATE[0]+10}" y="{GATE[1]+56}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{TXT}">quality gate</text>
<text x="{GATE[0]+10}" y="{GATE[1]+72}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{MUTED}">coverage + SARIF</text></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Animated process: application testing and security testing run in parallel and meet at a quality gate">
{DEFS}
<rect width="1200" height="300" rx="14" fill="url(#bg)" stroke="{CY}" stroke-opacity=".35"/>
<text x="60" y="44" font-family="{MONO}" font-size="12" fill="{CY}" letter-spacing="2">APPLICATION TESTING</text>
<text x="60" y="262" font-family="{MONO}" font-size="12" fill="{TEAL}" letter-spacing="2">SECURITY TESTING</text>
{lanes}{stages}{gate}{pkt("la", CY)}{pkt("ls", TEAL)}
</svg>'''


GROUPS = [
    ("Languages", [("Python", "python"), ("TypeScript", "typescript"), ("Java", "openjdk"), ("Swift", "swift"), ("SQL", "sqlite")]),
    ("Frameworks", [("pytest", "pytest"), ("Playwright", "playwright"), ("Selenium", "selenium"), ("Next.js", "nextdotjs"), ("FastAPI", "fastapi")]),
    ("Cloud & DevOps", [("GitHub Actions", "githubactions"), ("Jenkins", "jenkins"), ("Docker", "docker"), ("Cloudflare", "cloudflare")]),
    ("Tools", [("Burp Suite", "burpsuite"), ("OWASP ZAP", "owasp"), ("Postman", "postman")]),
]


def _color(hexv):
    r, g, b = (int(hexv[i:i + 2], 16) for i in (0, 2, 4))
    return "#e6edf3" if (0.299 * r + 0.587 * g + 0.114 * b) < 70 else "#" + hexv  # keep dark logos visible


def stack():
    rows, y = [], 20
    for g, items in GROUPS:
        rows.append(f'<text x="30" y="{y+30}" font-family="{MONO}" font-size="12" fill="{CY}" letter-spacing="2">{g.upper().replace("&", "&amp;")}</text>')
        for i, (label, slug) in enumerate(items):
            x = 200 + i * 192
            ic = ICONS.get(slug)
            glyph = (f'<g transform="translate({x+16} {y+11}) scale(1)"><path transform="scale(1)" d="{ic["d"]}" fill="{_color(ic["hex"])}"/></g>'
                     if ic else f'<circle cx="{x+28}" cy="{y+24}" r="4" fill="{TEAL}"/>')
            rows.append(f'''<g><rect x="{x}" y="{y}" width="178" height="48" rx="10" fill="#0a0f1a" stroke="{CY}" stroke-opacity=".28"/>
{glyph}<text x="{x+52}" y="{y+29}" font-family="{SANS}" font-size="14" font-weight="600" fill="{TXT}">{label}</text></g>''')
        y += 68
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{y+10}" viewBox="0 0 1200 {y+10}" role="img" aria-label="Tech stack">
{DEFS}
<rect width="1200" height="{y+10}" rx="14" fill="url(#bg)" stroke="{CY}" stroke-opacity=".35"/>
{"".join(rows)}</svg>'''
