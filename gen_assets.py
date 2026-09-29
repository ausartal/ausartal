"""Hero + panels matching the Achievement Hunter card style."""
import cairosvg
from pathlib import Path

OUT = Path(r"C:\Users\ahmad\Documents\College\Subjects\Data Mining\github-profile\assets")

INK = "#0F141B"
PANEL = "#161B22"
LINE = "#2A3340"
MUTED = "#8B949E"
PAPER = "#E6EDF3"
GOLD = "#C9A227"
CLAY = "#C47B6B"
GOLD2 = "#C4A05A"
SAGE = "#7FA88C"
STONE = "#9A9590"

# ── HERO — exact Achievement Hunter card language ─────────
# left: gold circle + star; middle: title serif, subtitle italic, badge row mono gold
# right: 4 stacked accent bars
hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="220" viewBox="0 0 920 220">
  <!-- card -->
  <rect x="8" y="8" width="904" height="204" rx="16" fill="{PANEL}"/>
  <rect x="8.5" y="8.5" width="903" height="203" rx="15.5" fill="none" stroke="{LINE}" stroke-width="1"/>

  <!-- gold star badge -->
  <circle cx="72" cy="110" r="32" stroke="{GOLD}" stroke-width="2" fill="{GOLD}" fill-opacity="0.12"/>
  <path d="M72 86 L 78 104 L 97 105 L 83 116 L 88 134 L 72 123 L 56 134 L 61 116 L 47 105 L 66 104 Z" fill="{GOLD}"/>

  <!-- title -->
  <text x="132" y="100" font-family="Georgia, 'Times New Roman', serif" font-size="32" fill="{PAPER}">Ausartal</text>

  <!-- subtitle -->
  <text x="132" y="132" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="{MUTED}">Creating is drawing, erasing, and drawing again —</text>
  <text x="132" y="156" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="{MUTED}">game dev, design, code, and sound.</text>

  <!-- badge line -->
  <text x="132" y="188" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" fill="{GOLD}" letter-spacing="1.2">GAME DEV  ·  DESIGN  ·  CODE  ·  SOUND</text>

  <!-- right accent bars -->
  <rect x="800" y="78" width="72" height="8" rx="4" fill="{CLAY}"/>
  <rect x="800" y="98" width="60" height="8" rx="4" fill="{GOLD2}"/>
  <rect x="800" y="118" width="68" height="8" rx="4" fill="{SAGE}"/>
  <rect x="800" y="138" width="48" height="8" rx="4" fill="{STONE}"/>
</svg>'''

# ── FIGURES — same card language ──────────────────────────
figures = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="180" viewBox="0 0 920 180">
  <rect x="8" y="8" width="904" height="164" rx="16" fill="{PANEL}"/>
  <rect x="8.5" y="8.5" width="903" height="163" rx="15.5" fill="none" stroke="{LINE}"/>

  <circle cx="56" cy="56" r="22" stroke="{GOLD}" stroke-width="1.6" fill="{GOLD}" fill-opacity="0.12"/>
  <path d="M56 40 L 60 52 L 73 52.5 L 63 60 L 66.5 72 L 56 65 L 45.5 72 L 49 60 L 39 52.5 L 52 52 Z" fill="{GOLD}"/>

  <text x="100" y="52" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="{PAPER}">Selected Figures</text>
  <text x="100" y="78" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{MUTED}">Craft measured in years, not weekend projects.</text>

  <rect x="800" y="40" width="72" height="8" rx="4" fill="{CLAY}"/>
  <rect x="800" y="60" width="60" height="8" rx="4" fill="{GOLD2}"/>
  <rect x="800" y="80" width="68" height="8" rx="4" fill="{SAGE}"/>
  <rect x="800" y="100" width="48" height="8" rx="4" fill="{STONE}"/>

  <text x="48" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{CLAY}">06</text>
  <text x="48" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">YEARS MAKING GAMES</text>

  <text x="250" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{GOLD2}">04</text>
  <text x="250" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">YEARS DESIGNING</text>

  <text x="450" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{SAGE}">05</text>
  <text x="450" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">YEARS WRITING CODE</text>

  <text x="650" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{STONE}">01</text>
  <text x="650" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">YEAR SCORING SOUND</text>
</svg>'''

# ── PRACTICE ──────────────────────────────────────────────
practice = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
  <rect x="8" y="8" width="384" height="284" rx="14" fill="{PANEL}"/>
  <rect x="8.5" y="8.5" width="383" height="283" rx="13.5" fill="none" stroke="{LINE}"/>

  <text x="32" y="44" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2.5">YEARS OF PRACTICE</text>
  <rect x="32" y="54" width="36" height="2" fill="{CLAY}"/>
  <rect x="72" y="54" width="36" height="2" fill="{GOLD2}"/>
  <rect x="112" y="54" width="36" height="2" fill="{SAGE}"/>
  <rect x="152" y="54" width="20" height="2" fill="{STONE}"/>

  <text x="32" y="98" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="{PAPER}">Game Development</text>
  <text x="360" y="98" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="{CLAY}" text-anchor="end">6</text>
  <rect x="32" y="110" width="328" height="5" rx="2.5" fill="#21262D"/>
  <rect x="32" y="110" width="328" height="5" rx="2.5" fill="{CLAY}"/>

  <text x="32" y="152" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="{PAPER}">Illustration &amp; Design</text>
  <text x="360" y="152" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="{GOLD2}" text-anchor="end">4</text>
  <rect x="32" y="164" width="328" height="5" rx="2.5" fill="#21262D"/>
  <rect x="32" y="164" width="218" height="5" rx="2.5" fill="{GOLD2}"/>

  <text x="32" y="206" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="{PAPER}">Code &amp; Engineering</text>
  <text x="360" y="206" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="{SAGE}" text-anchor="end">5</text>
  <rect x="32" y="218" width="328" height="5" rx="2.5" fill="#21262D"/>
  <rect x="32" y="218" width="273" height="5" rx="2.5" fill="{SAGE}"/>

  <text x="32" y="260" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="{PAPER}">Music &amp; Sound</text>
  <text x="360" y="260" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="{STONE}" text-anchor="end">1</text>
  <rect x="32" y="272" width="328" height="5" rx="2.5" fill="#21262D"/>
  <rect x="32" y="272" width="62" height="5" rx="2.5" fill="{STONE}"/>
</svg>'''

# ── STACK ─────────────────────────────────────────────────
stack = f'''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="210" viewBox="0 0 560 210">
  <rect x="8" y="8" width="544" height="194" rx="14" fill="{PANEL}"/>
  <rect x="8.5" y="8.5" width="543" height="193" rx="13.5" fill="none" stroke="{LINE}"/>

  <circle cx="48" cy="48" r="18" stroke="{GOLD}" stroke-width="1.4" fill="{GOLD}" fill-opacity="0.12"/>
  <path d="M48 36 L 51 46 L 62 46.5 L 54 53 L 56.5 63 L 48 57 L 39.5 63 L 42 53 L 34 46.5 L 45 46 Z" fill="{GOLD}"/>

  <text x="84" y="46" font-family="Georgia, 'Times New Roman', serif" font-size="18" fill="{PAPER}">Core Materials</text>
  <text x="84" y="68" font-family="Georgia, 'Times New Roman', serif" font-size="12" fill="{MUTED}">Tools I reach for without thinking.</text>

  <rect x="470" y="32" width="56" height="6" rx="3" fill="{CLAY}"/>
  <rect x="470" y="46" width="48" height="6" rx="3" fill="{GOLD2}"/>
  <rect x="470" y="60" width="52" height="6" rx="3" fill="{SAGE}"/>
  <rect x="470" y="74" width="36" height="6" rx="3" fill="{STONE}"/>

  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{PAPER}">
    <rect x="28" y="92" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="72" y="110" text-anchor="middle">Unreal</text>
    <rect x="124" y="92" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="168" y="110" text-anchor="middle">Godot 4</text>
    <rect x="220" y="92" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="264" y="110" text-anchor="middle">Unity</text>
    <rect x="316" y="92" width="132" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="382" y="110" text-anchor="middle">Pixel Game Maker</text>
    <rect x="456" y="92" width="80" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="496" y="110" text-anchor="middle">Roblox</text>

    <rect x="28" y="132" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.07" stroke="{PAPER}" stroke-opacity="0.3"/><text x="72" y="150" text-anchor="middle" fill="{MUTED}">Figma</text>
    <rect x="124" y="132" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.07" stroke="{PAPER}" stroke-opacity="0.3"/><text x="168" y="150" text-anchor="middle" fill="{MUTED}">Maya</text>
    <rect x="220" y="132" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.07" stroke="{PAPER}" stroke-opacity="0.3"/><text x="264" y="150" text-anchor="middle" fill="{MUTED}">Adobe</text>
    <rect x="316" y="132" width="112" height="28" rx="14" fill="{PAPER}" fill-opacity="0.07" stroke="{PAPER}" stroke-opacity="0.3"/><text x="372" y="150" text-anchor="middle" fill="{MUTED}">Clip Studio</text>
    <rect x="436" y="132" width="100" height="28" rx="14" fill="{PAPER}" fill-opacity="0.07" stroke="{PAPER}" stroke-opacity="0.3"/><text x="486" y="150" text-anchor="middle" fill="{MUTED}">Photoshop</text>

    <rect x="28" y="172" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="72" y="190" text-anchor="middle">C / C++</text>
    <rect x="124" y="172" width="64" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="156" y="190" text-anchor="middle">C#</text>
    <rect x="196" y="172" width="80" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="236" y="190" text-anchor="middle">Python</text>
    <rect x="284" y="172" width="64" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="316" y="190" text-anchor="middle">Java</text>
    <rect x="356" y="172" width="96" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="404" y="190" text-anchor="middle">TypeScript</text>
    <rect x="460" y="172" width="76" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.5"/><text x="498" y="190" text-anchor="middle">FL Studio</text>
  </g>
</svg>'''

# ── STATS ─────────────────────────────────────────────────
stats = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="180" viewBox="0 0 920 180">
  <rect x="8" y="8" width="904" height="164" rx="16" fill="{PANEL}"/>
  <rect x="8.5" y="8.5" width="903" height="163" rx="15.5" fill="none" stroke="{LINE}"/>

  <circle cx="56" cy="56" r="22" stroke="{GOLD}" stroke-width="1.6" fill="{GOLD}" fill-opacity="0.12"/>
  <path d="M56 40 L 60 52 L 73 52.5 L 63 60 L 66.5 72 L 56 65 L 45.5 72 L 49 60 L 39 52.5 L 52 52 Z" fill="{GOLD}"/>

  <text x="100" y="52" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="{PAPER}">GitHub Snapshot</text>
  <text x="100" y="78" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{MUTED}">Public work and practice, in plain numbers.</text>

  <rect x="800" y="40" width="72" height="8" rx="4" fill="{CLAY}"/>
  <rect x="800" y="60" width="60" height="8" rx="4" fill="{GOLD2}"/>
  <rect x="800" y="80" width="68" height="8" rx="4" fill="{SAGE}"/>
  <rect x="800" y="100" width="48" height="8" rx="4" fill="{STONE}"/>

  <text x="48" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{PAPER}">16+</text>
  <text x="48" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">REPOSITORIES</text>

  <text x="250" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{CLAY}">34</text>
  <text x="250" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">MERGED PULL REQUESTS</text>

  <text x="500" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{GOLD2}">06</text>
  <text x="500" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">YEARS GAMES</text>

  <text x="700" y="140" font-family="Georgia, 'Times New Roman', serif" font-size="40" fill="{SAGE}">05</text>
  <text x="700" y="162" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="1.3">YEARS CODE</text>
</svg>'''

for name, svg, w in [
    ("hero.svg", hero, 920),
    ("figures.svg", figures, 920),
    ("practice.svg", practice, 800),
    ("stack.svg", stack, 920),
    ("stats.svg", stats, 920),
]:
    (OUT / name).write_text(svg, encoding="utf-8")
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(OUT / name.replace(".svg", ".png")), output_width=w)
    print(name, "ok")
print("done")
