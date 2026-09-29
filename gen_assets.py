"""Generate colored-but-flat hero + API-driven stats panel."""
import cairosvg, json, os, base64
from pathlib import Path
from urllib.request import Request, urlopen

OUT = Path(r"C:\Users\ahmad\Documents\College\Subjects\Data Mining\github-profile\assets")
TOKEN = os.environ.get("GH_TOKEN", "")

INK = "#0D1117"
PANEL = "#11171F"
LINE = "#2A3340"
MUTED = "#8B949E"
PAPER = "#E6EDF3"

# warm, flat accents (no glow / no radial)
CLAY = "#D08770"
GOLD = "#D4A857"
SAGE = "#8FBC8F"
STONE = "#A8A29E"

def gh(path):
    req = Request(f"https://api.github.com{path}", headers={
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": "ausartal-profile",
        "Accept": "application/vnd.github+json",
    })
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())

user = gh("/users/ausartal")
repos = gh("/users/ausartal/repos?per_page=100&sort=updated")
langs = {}
for repo in repos:
    if repo.get("fork") or not repo.get("language"):
        continue
    langs[repo["language"]] = langs.get(repo["language"], 0) + 1
top = sorted(langs.items(), key=lambda x: -x[1])[:5]
maxc = top[0][1] if top else 1

# ── HERO: colored, flat ──────────────────────────────────
hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="250" viewBox="0 0 920 250">
  <rect width="920" height="250" rx="12" fill="{INK}"/>
  <rect x="0.5" y="0.5" width="919" height="249" rx="11.5" fill="none" stroke="{LINE}"/>

  <!-- color rules, flat -->
  <rect x="48" y="40" width="28" height="3" fill="{CLAY}"/>
  <rect x="80" y="40" width="28" height="3" fill="{GOLD}"/>
  <rect x="112" y="40" width="28" height="3" fill="{SAGE}"/>
  <rect x="144" y="40" width="28" height="3" fill="{STONE}"/>

  <text x="48" y="78" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{MUTED}" letter-spacing="3.5">PORTFOLIO</text>

  <text x="46" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="{PAPER}" letter-spacing="-1.2">Ausartal</text>

  <text x="48" y="178" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="18" fill="{MUTED}">Creating is drawing, erasing, and drawing again.</text>

  <!-- colored flat chips -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">
    <rect x="48" y="200" width="128" height="30" rx="2" fill="{CLAY}" fill-opacity="0.18" stroke="{CLAY}" stroke-opacity="0.7"/>
    <text x="112" y="220" text-anchor="middle" fill="{CLAY}" letter-spacing="1.2">GAME DEV · 6 YRS</text>

    <rect x="188" y="200" width="120" height="30" rx="2" fill="{GOLD}" fill-opacity="0.18" stroke="{GOLD}" stroke-opacity="0.7"/>
    <text x="248" y="220" text-anchor="middle" fill="{GOLD}" letter-spacing="1.2">DESIGN · 4 YRS</text>

    <rect x="320" y="200" width="112" height="30" rx="2" fill="{SAGE}" fill-opacity="0.18" stroke="{SAGE}" stroke-opacity="0.7"/>
    <text x="376" y="220" text-anchor="middle" fill="{SAGE}" letter-spacing="1.2">CODE · 5 YRS</text>

    <rect x="444" y="200" width="116" height="30" rx="2" fill="{STONE}" fill-opacity="0.15" stroke="{STONE}" stroke-opacity="0.7"/>
    <text x="502" y="220" text-anchor="middle" fill="{STONE}" letter-spacing="1.2">SOUND · 1 YR</text>
  </g>

  <!-- flat geometric, no glow -->
  <g fill="none" stroke-width="1.2">
    <rect x="780" y="70" width="44" height="44" stroke="{CLAY}" stroke-opacity="0.75"/>
    <line x1="780" y1="70" x2="824" y2="114" stroke="{CLAY}" stroke-opacity="0.45"/>
    <rect x="836" y="70" width="44" height="44" stroke="{GOLD}" stroke-opacity="0.65"/>
    <rect x="780" y="130" width="44" height="44" stroke="{SAGE}" stroke-opacity="0.55"/>
    <rect x="836" y="130" width="44" height="44" stroke="{STONE}" stroke-opacity="0.45"/>
  </g>
  <g>
    <rect x="786" y="76" width="32" height="32" fill="{CLAY}" fill-opacity="0.25"/>
    <rect x="842" y="76" width="32" height="32" fill="{GOLD}" fill-opacity="0.22"/>
    <rect x="786" y="136" width="32" height="32" fill="{SAGE}" fill-opacity="0.2"/>
    <rect x="842" y="136" width="32" height="32" fill="{STONE}" fill-opacity="0.18"/>
  </g>
</svg>'''

# ── FIGURES: colored numbers, flat ───────────────────────
figures = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="180" viewBox="0 0 920 180">
  <rect width="920" height="180" rx="10" fill="{INK}"/>
  <rect x="0.5" y="0.5" width="919" height="179" rx="9.5" fill="none" stroke="{LINE}"/>

  <text x="36" y="36" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="3">SELECTED FIGURES</text>
  <rect x="36" y="46" width="28" height="2" fill="{CLAY}"/>
  <rect x="68" y="46" width="28" height="2" fill="{GOLD}"/>
  <rect x="100" y="46" width="28" height="2" fill="{SAGE}"/>
  <rect x="132" y="46" width="28" height="2" fill="{STONE}"/>

  <text x="36" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{CLAY}">06</text>
  <text x="36" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">years making games</text>
  <text x="36" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">UNREAL · GODOT · UNITY · RBLX</text>

  <line x1="230" y1="64" x2="230" y2="158" stroke="{LINE}"/>

  <text x="270" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{GOLD}">04</text>
  <text x="270" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">years designing</text>
  <text x="270" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">FIGMA · MAYA · ADOBE · CSP</text>

  <line x1="470" y1="64" x2="470" y2="158" stroke="{LINE}"/>

  <text x="510" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{SAGE}">05</text>
  <text x="510" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">years writing code</text>
  <text x="510" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">C · C++ · C# · PYTHON · TS</text>

  <line x1="710" y1="64" x2="710" y2="158" stroke="{LINE}"/>

  <text x="750" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{STONE}">01</text>
  <text x="750" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">year scoring sound</text>
  <text x="750" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">FL STUDIO · CAKEWALK</text>
</svg>'''

# ── PRACTICE bars: colored flat ──────────────────────────
practice = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
  <rect width="400" height="300" rx="10" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="399" height="299" rx="9.5" fill="none" stroke="{LINE}"/>

  <text x="28" y="40" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2.5">YEARS OF PRACTICE</text>
  <rect x="28" y="50" width="48" height="2" fill="{CLAY}"/>

  <text x="28" y="92" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Game Development</text>
  <text x="360" y="92" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{CLAY}" text-anchor="end">6</text>
  <rect x="28" y="104" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="104" width="332" height="4" fill="{CLAY}"/>

  <text x="28" y="146" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Illustration &amp; Design</text>
  <text x="360" y="146" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{GOLD}" text-anchor="end">4</text>
  <rect x="28" y="158" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="158" width="221" height="4" fill="{GOLD}"/>

  <text x="28" y="200" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Code &amp; Engineering</text>
  <text x="360" y="200" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{SAGE}" text-anchor="end">5</text>
  <rect x="28" y="212" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="212" width="276" height="4" fill="{SAGE}"/>

  <text x="28" y="254" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Music &amp; Sound</text>
  <text x="360" y="254" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{STONE}" text-anchor="end">1</text>
  <rect x="28" y="266" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="266" width="62" height="4" fill="{STONE}"/>
</svg>'''

# ── STATS panel from live API (replaces broken vercel widgets) ──
def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

lang_rows = []
colors = [CLAY, GOLD, SAGE, STONE, MUTED]
for i, (name, count) in enumerate(top):
    y = 86 + i * 28
    w = int(180 * (count / maxc))
    c = colors[i % len(colors)]
    lang_rows.append(
        f'<text x="36" y="{y}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" fill="{PAPER}">{esc(name)}</text>\n'
        f'  <rect x="160" y="{y-10}" width="180" height="6" fill="#21262D"/>\n'
        f'  <rect x="160" y="{y-10}" width="{max(w,8)}" height="6" fill="{c}"/>\n'
        f'  <text x="356" y="{y}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{MUTED}">{count}</text>'
    )

stars = sum(r.get("stargazers_count", 0) or 0 for r in repos)
stats = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="230" viewBox="0 0 920 230">
  <rect width="920" height="230" rx="10" fill="{INK}"/>
  <rect x="0.5" y="0.5" width="919" height="229" rx="9.5" fill="none" stroke="{LINE}"/>

  <text x="36" y="36" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="3">GITHUB SNAPSHOT</text>
  <rect x="36" y="46" width="28" height="2" fill="{CLAY}"/>
  <rect x="68" y="46" width="28" height="2" fill="{GOLD}"/>
  <rect x="100" y="46" width="28" height="2" fill="{SAGE}"/>

  <!-- metrics -->
  <text x="36" y="96" font-family="Georgia, 'Times New Roman', serif" font-size="36" fill="{PAPER}">{user.get('public_repos', 0)}</text>
  <text x="36" y="118" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.5">REPOSITORIES</text>

  <text x="150" y="96" font-family="Georgia, 'Times New Roman', serif" font-size="36" fill="{CLAY}">{user.get('followers', 0)}</text>
  <text x="150" y="118" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.5">FOLLOWERS</text>

  <text x="260" y="96" font-family="Georgia, 'Times New Roman', serif" font-size="36" fill="{GOLD}">{stars}</text>
  <text x="260" y="118" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.5">STARS EARNED</text>

  <text x="380" y="96" font-family="Georgia, 'Times New Roman', serif" font-size="36" fill="{SAGE}">{len(repos)}</text>
  <text x="380" y="118" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.5">PUBLIC WORKS</text>

  <line x1="500" y1="56" x2="500" y2="210" stroke="{LINE}"/>

  <text x="530" y="40" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2">TOP LANGUAGES</text>
  {"".join(f'<text x="530" y="{70+i*22}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{colors[i%len(colors)]}">{esc(n)}</text>' for i, (n, c) in enumerate(top))}

  <!-- small color legend -->
  <rect x="36" y="160" width="28" height="2" fill="{CLAY}"/>
  <rect x="68" y="160" width="28" height="2" fill="{GOLD}"/>
  <rect x="100" y="160" width="28" height="2" fill="{SAGE}"/>
  <rect x="132" y="160" width="28" height="2" fill="{STONE}"/>
  <text x="36" y="190" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="13" fill="{MUTED}">data pulled from the GitHub profile</text>
</svg>'''

# ── STACK: keep monochrome (user asked earlier) ──────────
stack = f'''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="190" viewBox="0 0 560 190">
  <rect width="560" height="190" rx="10" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="559" height="189" rx="9.5" fill="none" stroke="{LINE}"/>
  <text x="24" y="32" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2.5">CORE MATERIALS</text>
  <rect x="24" y="42" width="40" height="1" fill="{PAPER}" opacity="0.5"/>

  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{PAPER}">
    <rect x="24" y="58" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="68" y="76" text-anchor="middle">Unreal</text>
    <rect x="120" y="58" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="164" y="76" text-anchor="middle">Godot 4</text>
    <rect x="216" y="58" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="260" y="76" text-anchor="middle">Unity</text>
    <rect x="312" y="58" width="132" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="378" y="76" text-anchor="middle">Pixel Game Maker</text>
    <rect x="452" y="58" width="84" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="494" y="76" text-anchor="middle">Roblox</text>

    <rect x="24" y="98" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/><text x="68" y="116" text-anchor="middle" fill="{MUTED}">Figma</text>
    <rect x="120" y="98" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/><text x="164" y="116" text-anchor="middle" fill="{MUTED}">Maya</text>
    <rect x="216" y="98" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/><text x="260" y="116" text-anchor="middle" fill="{MUTED}">Adobe</text>
    <rect x="312" y="98" width="112" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/><text x="368" y="116" text-anchor="middle" fill="{MUTED}">Clip Studio</text>
    <rect x="432" y="98" width="104" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/><text x="484" y="116" text-anchor="middle" fill="{MUTED}">Photoshop</text>

    <rect x="24" y="138" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="68" y="156" text-anchor="middle">C / C++</text>
    <rect x="120" y="138" width="64" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="152" y="156" text-anchor="middle">C#</text>
    <rect x="192" y="138" width="80" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="232" y="156" text-anchor="middle">Python</text>
    <rect x="280" y="138" width="64" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="312" y="156" text-anchor="middle">Java</text>
    <rect x="352" y="138" width="96" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="400" y="156" text-anchor="middle">TypeScript</text>
    <rect x="456" y="138" width="80" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/><text x="496" y="156" text-anchor="middle">FL Studio</text>
  </g>
</svg>'''

for name, svg in [("hero.svg", hero), ("figures.svg", figures), ("practice.svg", practice), ("stats.svg", stats), ("stack.svg", stack)]:
    (OUT / name).write_text(svg, encoding="utf-8")
    w = 800 if name == "practice.svg" else 920
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(OUT / name.replace(".svg", ".png")), output_width=w)
    print(f"{name} ok")

print("done")
