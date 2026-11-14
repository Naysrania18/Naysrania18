"""Build assets/activity.svg and assets/languages.svg from real GitHub data (needs `gh` logged in).
Run: python scripts/build_activity.py <username>"""
import collections, datetime, json, subprocess, sys
from pathlib import Path
from build_cyber_assets import DEFS, MONO, SANS, CY, TEAL, TXT, MUTED

OUT = Path(__file__).resolve().parent.parent / "assets"
QUERY = '''query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}
repositories(ownerAffiliations:OWNER,isFork:false,first:100,privacy:PUBLIC){nodes{primaryLanguage{name}}}}}'''


def fetch(user):
    r = subprocess.run(["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"u={user}"], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)["data"]["user"]


def activity(cal):
    weeks, cell, gap, x0, y0 = cal["weeks"], 17, 4, 40, 74
    mx = max((d["contributionCount"] for w in weeks for d in w["contributionDays"]), default=1) or 1
    def op(n):
        if n == 0: return 0.07
        r = n / mx
        return 0.3 if r <= .25 else 0.55 if r <= .5 else 0.8 if r <= .75 else 1.0
    rects, months, last = [], [], None
    for i, w in enumerate(weeks):
        for d in w["contributionDays"]:
            wd = datetime.date.fromisoformat(d["date"]).weekday()  # Mon=0
            n = d["contributionCount"]
            rects.append(f'<rect x="{x0+i*(cell+gap)}" y="{y0+wd*(cell+gap)}" width="{cell}" height="{cell}" rx="3" fill="{CY}" fill-opacity="{op(n)}"><title>{d["date"]}: {n}</title></rect>')
        m = datetime.date.fromisoformat(w["contributionDays"][0]["date"]).strftime("%b")
        if m != last:
            months.append(f'<text x="{x0+i*(cell+gap)}" y="{y0-10}" font-family="{MONO}" font-size="11" fill="{MUTED}">{m}</text>'); last = m
    days = "".join(f'<text x="14" y="{y0+k*(cell+gap)+12}" font-family="{MONO}" font-size="10" fill="{MUTED}">{t}</text>' for k, t in ((0, "Mon"), (2, "Wed"), (4, "Fri")))
    first, lastd = weeks[0]["contributionDays"][0]["date"], weeks[-1]["contributionDays"][-1]["date"]
    h = y0 + 7 * (cell + gap) + 16
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="{cal["totalContributions"]} contributions between {first} and {lastd}">
{DEFS}
<rect width="1200" height="{h}" rx="14" fill="url(#bg)" stroke="{CY}" stroke-opacity=".35"/>
<text x="40" y="36" font-family="{SANS}" font-size="20" font-weight="700" fill="{TXT}"><tspan fill="{CY}">{cal["totalContributions"]}</tspan> contributions in the last year</text>
<text x="1160" y="36" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}">{first} to {lastd}</text>
{days}{"".join(months)}{"".join(rects)}</svg>'''


def languages(nodes):
    c = collections.Counter(n["primaryLanguage"]["name"] for n in nodes if n["primaryLanguage"])
    total = sum(c.values()); rows = []
    for i, (name, k) in enumerate(c.most_common(6)):
        y = 70 + i * 34
        rows.append(f'''<text x="40" y="{y+14}" font-family="{SANS}" font-size="14" font-weight="600" fill="{TXT}">{name}</text>
<rect x="190" y="{y}" width="820" height="18" rx="9" fill="{CY}" fill-opacity=".08"/>
<rect x="190" y="{y}" width="{max(820*k/total, 14):.0f}" height="18" rx="9" fill="{CY}" filter="url(#glow)"/>
<text x="1160" y="{y+14}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUTED}">{k} repos</text>''')
    h = 70 + len(rows) * 34 + 14
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="Public repositories by primary language">
{DEFS}
<rect width="1200" height="{h}" rx="14" fill="url(#bg)" stroke="{CY}" stroke-opacity=".35"/>
<text x="40" y="36" font-family="{SANS}" font-size="20" font-weight="700" fill="{TXT}">Public repositories by language</text>
{"".join(rows)}</svg>'''


if __name__ == "__main__":
    u = fetch(sys.argv[1] if len(sys.argv) > 1 else "Naysrania18")
    (OUT / "activity.svg").write_text(activity(u["contributionsCollection"]["contributionCalendar"]), encoding="utf-8")
    (OUT / "languages.svg").write_text(languages(u["repositories"]["nodes"]), encoding="utf-8")
    print("wrote activity.svg languages.svg")
