"""Profile v3 assets (900 wide, CSS-only animation, no external fonts, no JavaScript).
Run: python scripts/build_profile_assets.py"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
ICONS = json.loads((Path(__file__).parent / "icons.json").read_text())

BG1, BG2 = "#0a0f1a", "#0d1117"
CY, TEAL, TXT, MUTED = "#00e5ff", "#14f1d9", "#e6edf3", "#5b7a8a"
AMBER, RED = "#ef9f27", "#f09595"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono','Courier New',monospace"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

DEFS = f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>'''

REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none !important}}"


def pct(sec, total):
    return sec / total * 100


# ---------------------------------------------------------------- terminal card
def terminal():
    total = 12.0  # seconds, loop
    lines = [  # (prompt, output, output colour)
        ("whoami", "Sandeep Kumar Naysrania", TXT),
        ("role", "Quality and security engineer", CY),
        ("focus", "test automation / API security / AI-assisted QA", TXT),
        ("location", "Ireland", TXT),
    ]
    css, body = [], []
    y0, step = 112, 44
    for i, (cmd, out, col) in enumerate(lines):
        y = y0 + i * step
        t0 = 0.4 + i * 2.2            # start typing this output
        dur = 1.4
        a, b = pct(t0, total), pct(t0 + dur, total)
        n = max(len(out), 8)
        css.append(f"@keyframes r{i}{{0%,{a:.2f}%{{transform:translateX(0)}}{b:.2f}%,100%{{transform:translateX(760px)}}}}")
        css.append(f".r{i}{{animation:r{i} {total}s steps({n},end) infinite}}")
        body.append(f'<text x="32" y="{y}" font-family="{MONO}" font-size="15" fill="{TEAL}">$ {cmd}</text>')
        body.append(f'<text x="170" y="{y}" font-family="{MONO}" font-size="17" font-weight="600" fill="{col}">{out}</text>')
        body.append(f'<rect class="r{i}" x="166" y="{y-20}" width="730" height="30" fill="{BG2}"/>')
    css.append(f"@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}.cur{{animation:blink 1s step-end infinite}}")
    cy = y0 + (len(lines) - 1) * step
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{y0+len(lines)*step+10}" viewBox="0 0 900 {y0+len(lines)*step+10}" role="img" aria-label="Terminal window: Sandeep Kumar Naysrania, quality and security engineer, test automation, API security, AI-assisted QA, Ireland">
<style>{"".join(css)}{REDUCED}</style>
{DEFS}
<rect x="0.75" y="0.75" width="898.5" height="{y0+len(lines)*step+8.5}" rx="12" fill="{BG2}" stroke="{CY}" stroke-opacity=".5" stroke-width="1.5"/>
<path d="M1 44 H899" stroke="{CY}" stroke-opacity=".2"/>
<circle cx="28" cy="23" r="6" fill="{MUTED}" fill-opacity=".7"/><circle cx="50" cy="23" r="6" fill="{MUTED}" fill-opacity=".5"/><circle cx="72" cy="23" r="6" fill="{TEAL}"/>
<text x="450" y="28" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{MUTED}">naysrania18 ~ profile</text>
{"".join(body)}
<rect class="cur" x="{170}" y="{cy+34}" width="10" height="18" fill="{CY}" filter="url(#glow)"/>
<text x="32" y="{cy+48}" font-family="{MONO}" font-size="15" fill="{TEAL}">$</text>
</svg>'''


# ---------------------------------------------------------------- metrics pills
PILLS = ["210+ Python tests", "66 Java tests", "20+ security labs documented",
         "90/85/90 coverage gates", "22-finding LLM triage evaluation", "4 planted defects documented"]


def pills():
    rows, x, y, W, H = [], 0, 0, 900, 40
    pad, gap = 22, 14
    items = []
    for t in PILLS:
        w = int(len(t) * 8.4 + pad * 2)
        items.append((t, w))
    # two balanced rows
    r1, r2 = items[:3], items[3:]
    out = []
    for ri, row in enumerate((r1, r2)):
        total = sum(w for _, w in row) + gap * (len(row) - 1)
        x = (W - total) / 2
        y = 8 + ri * 52
        for t, w in row:
            out.append(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="{H}" rx="20" fill="{BG1}" stroke="{CY}" stroke-opacity=".55" stroke-width="1.3"/>'
                       f'<circle cx="{x+16:.0f}" cy="{y+20}" r="3.5" fill="{TEAL}"/>'
                       f'<text x="{x+30:.0f}" y="{y+25}" font-family="{MONO}" font-size="13.5" fill="{TXT}">{t}</text>')
            x += w + gap
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="108" viewBox="0 0 900 108" role="img" aria-label="Metrics: {', '.join(PILLS)}">
{DEFS}{"".join(out)}</svg>'''


# ---------------------------------------------------------------- SSDLC workflow
STAGES = [
    ("01", "Plan", "threat model", "Plan & threat model", "before code is written", [
        ("Test strategy", "acceptance criteria, edge cases", "defined", TEAL),
        ("Threat model", "STRIDE, trust boundaries", "mapped", TEAL)]),
    ("02", "Code", "static analysis", "Code & static analysis", "CI, pre-merge gates", [
        ("Secrets + lint", "GitLeaks, markdownlint", "pass", TEAL),
        ("Unit + integration", "pytest, Vitest, TestNG", "pass", TEAL),
        ("SAST", "Bandit, Semgrep", "2 flagged", AMBER)]),
    ("03", "Build", "infra checks", "Build & infrastructure", "before deployment", [
        ("Container + CI", "Docker, GitHub Actions", "pass", TEAL),
        ("Resilience", "Toxiproxy fault injection", "1 gap", AMBER)]),
    ("04", "Test", "dynamic + manual", "Dynamic QA & security", "staging environment", [
        ("E2E + API QA", "Playwright, Postman, Pact", "pass", TEAL),
        ("Automated DAST", "OWASP ZAP", "pass", TEAL),
        ("Manual pentest", "Burp Suite, OWASP Top 10", "IDOR found", RED)]),
    ("05", "Release", "gate + monitor", "Release, monitor & remediate", "production", [
        ("Retest loop", "triage, fix, verify", "all fixed", TEAL),
        ("Release gate", "no critical or high open", "approved", TEAL),
        ("Monitoring", "smoke tests, runtime alerts", "live", TEAL)]),
]
LOOP = 15.0
NX = [90 + i * 180 for i in range(5)]


def workflow():
    css, svg = [], []
    css.append(f"*{{animation-duration:{LOOP}s;animation-iteration-count:infinite;animation-timing-function:linear}}")
    # progress line + packet
    css.append("@keyframes prog{0%,17%{transform:scaleX(0)}20%,37%{transform:scaleX(.25)}40%,57%{transform:scaleX(.5)}60%,77%{transform:scaleX(.75)}80%,100%{transform:scaleX(1)}}")
    css.append("@keyframes hop{0%,17%{transform:translateX(0)}20%,37%{transform:translateX(180px)}40%,57%{transform:translateX(360px)}60%,77%{transform:translateX(540px)}80%,100%{transform:translateX(720px)}}")
    css.append(".prog{transform-box:fill-box;transform-origin:left center;animation-name:prog;transform:scaleX(1)}.hop{animation-name:hop;transform:translateX(720px)}")
    # nodes: dim -> cyan (active) -> teal (done)
    for k in range(5):
        a, b = k * 20, (k + 1) * 20
        css.append(f"@keyframes n{k}{{0%,{max(a-0.01,0):.2f}%{{stroke:{MUTED};fill:{BG1}}}{a:.2f}%,{b-0.5:.2f}%{{stroke:{CY};fill:#06222b}}{b:.2f}%,99.9%{{stroke:{TEAL};fill:#06231f}}100%{{stroke:{MUTED};fill:{BG1}}}}}"
                   f"@keyframes g{k}{{0%,{max(a-0.01,0):.2f}%{{opacity:0}}{a:.2f}%,{b-0.5:.2f}%{{opacity:.9}}{b:.2f}%,100%{{opacity:0}}}}"
                   f".n{k}{{animation-name:n{k};stroke:{TEAL};fill:#06231f}}.g{k}{{animation-name:g{k};opacity:0}}")
    # panels and rows
    for k, st in enumerate(STAGES):
        a, b = k * 20, (k + 1) * 20
        fade = 0.8
        css.append(f"@keyframes p{k}{{0%,{max(a-0.01,0):.2f}%{{opacity:0}}{a+fade:.2f}%,{b-fade:.2f}%{{opacity:1}}{b:.2f}%,100%{{opacity:0}}}}"
                   f".p{k}{{animation-name:p{k};opacity:{1 if k == 3 else 0}}}")
        for j in range(len(st[5])):
            t = k * 3 + 0.5 + j * 0.65
            s0, s1 = pct(t, LOOP), pct(t + 0.45, LOOP)
            css.append(f"@keyframes r{k}{j}{{0%,{s0:.2f}%{{opacity:0;transform:translateX(-18px)}}{s1:.2f}%,{b-fade:.2f}%{{opacity:1;transform:translateX(0)}}{b:.2f}%,100%{{opacity:0;transform:translateX(0)}}}}"
                       f".r{k}{j}{{animation-name:r{k}{j}}}")
    css.append(REDUCED)

    # circuit traces
    traces = (f'<path d="M0 150 H30 L50 130 H130" stroke="{CY}" stroke-opacity=".15" fill="none"/>'
              f'<path d="M900 150 H870 L850 130 H770" stroke="{CY}" stroke-opacity=".15" fill="none"/>'
              f'<path d="M0 420 H60 L80 440 H170" stroke="{CY}" stroke-opacity=".15" fill="none"/>'
              f'<path d="M900 420 H840 L820 440 H730" stroke="{CY}" stroke-opacity=".15" fill="none"/>')
    # track
    svg.append(f'<line x1="{NX[0]}" y1="70" x2="{NX[-1]}" y2="70" stroke="{MUTED}" stroke-opacity=".5" stroke-width="3"/>')
    svg.append(f'<rect class="prog" x="{NX[0]}" y="68.5" width="{NX[-1]-NX[0]}" height="3" fill="{TEAL}"/>')
    for k, (num, name, sub, *_r) in enumerate(STAGES):
        x = NX[k]
        svg.append(f'<circle class="g{k}" cx="{x}" cy="70" r="26" fill="{CY}" filter="url(#glow)" opacity="0" fill-opacity=".25"/>')
        svg.append(f'<circle class="n{k}" cx="{x}" cy="70" r="19" stroke-width="2.5"/>')
        svg.append(f'<text x="{x}" y="75" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="{TXT}">{num}</text>')
        svg.append(f'<text x="{x}" y="112" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="600" fill="{TXT}">{name}</text>')
        svg.append(f'<text x="{x}" y="130" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{MUTED}">{sub}</text>')
    svg.append(f'<circle class="hop" cx="{NX[0]}" cy="34" r="4.5" fill="{CY}" filter="url(#glow)"/>')

    # detail panel frame
    svg.append(f'<rect x="40" y="152" width="820" height="232" rx="12" fill="{BG1}" stroke="{CY}" stroke-opacity=".35" stroke-width="1.3"/>')
    for k, (num, name, sub, title, ctx, rows) in enumerate(STAGES):
        g = [f'<g class="p{k}">',
             f'<text x="68" y="188" font-family="{SANS}" font-size="18" font-weight="700" fill="{CY}">{num}  {title.replace("&", "&amp;")}</text>',
             f'<text x="832" y="188" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUTED}">{ctx}</text>',
             f'<line x1="68" y1="202" x2="832" y2="202" stroke="{CY}" stroke-opacity=".2"/>']
        for j, (chk, tools, status, col) in enumerate(rows):
            y = 238 + j * 44
            g.append(f'<g class="r{k}{j}"><circle cx="76" cy="{y-5}" r="4" fill="{col}"/>'
                     f'<text x="92" y="{y}" font-family="{SANS}" font-size="15" font-weight="600" fill="{TXT}">{chk}</text>'
                     f'<text x="330" y="{y}" font-family="{MONO}" font-size="13" fill="{MUTED}">{tools}</text>'
                     f'<rect x="690" y="{y-19}" width="142" height="28" rx="14" fill="{col}" fill-opacity=".14" stroke="{col}" stroke-opacity=".7"/>'
                     f'<text x="761" y="{y}" text-anchor="middle" font-family="{MONO}" font-size="12.5" font-weight="600" fill="{col}">{status}</text></g>')
        g.append("</g>")
        svg.append("".join(g))
    svg.append(f'<text x="450" y="412" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{TXT}">shift-left: every stage is a gate, not only the last one</text>')
    svg.append(f'<text x="450" y="432" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{MUTED}">findings shown are illustrative examples, not client results</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="450" viewBox="0 0 900 450" role="img" aria-label="Animated secure development lifecycle: Plan, Code, Build, Test, Release. Each stage is a gate with automated and manual checks.">
<style>{"".join(css)}</style>
{DEFS}
<rect x="0.75" y="0.75" width="898.5" height="448.5" rx="14" fill="url(#bg)" stroke="{CY}" stroke-opacity=".4" stroke-width="1.5"/>
{traces}{"".join(svg)}</svg>'''


# ---------------------------------------------------------------- contact badges (for-the-badge style)
def badge(label, icon, color, value):
    ic = ICONS[icon]
    w = 40 + len(label) * 11 + 22
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="38" viewBox="0 0 {w} 38" role="img" aria-label="{label}: {value}">
<rect x="0.75" y="0.75" width="{w-1.5}" height="36.5" rx="6" fill="{BG1}" stroke="{CY}" stroke-opacity=".6" stroke-width="1.3"/>
<g transform="translate(14 8) scale(.92)"><path d="{ic["d"]}" fill="{color}"/></g>
<text x="44" y="24" font-family="{SANS}" font-size="13" font-weight="800" letter-spacing="1.4" fill="{TXT}">{label.upper()}</text>
</svg>'''


# ---------------------------------------------------------------- GitHub stats card + light variants
def stats_card(data):
    cells = [(str(data["contrib"]), "contributions, last 12 months"), (str(data["repos"]), "public repositories"), (str(data["prs"]), "pull requests")]
    out = []
    for i, (n, l) in enumerate(cells):
        x = 24 + i * 292
        out.append(f'<rect x="{x}" y="22" width="268" height="104" rx="12" fill="{BG1}" stroke="{CY}" stroke-opacity=".5" stroke-width="1.3"/>'
                   f'<text x="{x+134}" y="76" text-anchor="middle" font-family="{SANS}" font-size="40" font-weight="700" fill="{CY}">{n}</text>'
                   f'<text x="{x+134}" y="106" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{TXT}">{l}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="148" viewBox="0 0 900 148" role="img" aria-label="GitHub: {data["contrib"]} contributions in the last 12 months, {data["repos"]} public repositories, {data["prs"]} pull requests">
{DEFS}{"".join(out)}</svg>'''


LIGHT = {"#0a0f1a": "#ffffff", "#0d1117": "#f6f8fa", "#00e5ff": "#0e7490", "#14f1d9": "#0f766e",
         "#e6edf3": "#0f172a", "#8b949e": "#57606a", "#5b7a8a": "#57606a", "#06222b": "#e6f6f8", "#06231f": "#e6f6f4"}


def to_light(svg):
    for a, b in LIGHT.items():
        svg = svg.replace(a, b)
    return svg


def main(data):
    OUT.mkdir(exist_ok=True)
    files = {
        "terminal-card.svg": terminal(), "metrics-pills.svg": pills(), "ssdlc-workflow.svg": workflow(),
        "badge-linkedin.svg": badge("LinkedIn", "linkedin", "#0A66C2", "sandeepnaysrania"),
        "badge-github.svg": badge("GitHub", "github", "#e6edf3", "Naysrania18"),
    }
    for n, s in files.items():
        (OUT / n).write_text(s, encoding="utf-8")
    card = stats_card(data)
    (OUT / "github-stats-dark.svg").write_text(card, encoding="utf-8")
    (OUT / "github-stats-light.svg").write_text(to_light(card), encoding="utf-8")
    return list(files) + ["github-stats-dark.svg", "github-stats-light.svg"]


if __name__ == "__main__":
    import build_activity as ba
    u = ba.fetch("Naysrania18")
    cc = u["contributionsCollection"]
    import subprocess
    r = subprocess.run(["gh", "api", "graphql", "-f", "query=query{user(login:\"Naysrania18\"){contributionsCollection{totalPullRequestContributions}repositories(ownerAffiliations:OWNER,isFork:false,privacy:PUBLIC){totalCount}}}"], capture_output=True, text=True, check=True)
    d = json.loads(r.stdout)["data"]["user"]
    data = {"contrib": cc["contributionCalendar"]["totalContributions"], "repos": d["repositories"]["totalCount"], "prs": d["contributionsCollection"]["totalPullRequestContributions"]}
    print("wrote", main(data), data)
    # light/dark variants of the year heatmap
    act = (OUT / "activity.svg").read_text(encoding="utf-8")
    (OUT / "activity-dark.svg").write_text(act, encoding="utf-8")
    (OUT / "activity-light.svg").write_text(to_light(act), encoding="utf-8")
    print("wrote activity-dark.svg activity-light.svg")
