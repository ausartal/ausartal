"""Generate polished profile assets as SVG → PNG."""
import cairosvg
from pathlib import Path

OUT = Path(r"C:\Users\ahmad\Documents\College\Subjects\Data Mining\github-profile\assets")
OUT.mkdir(parents=True, exist_ok=True)

# ─── 1. HERO ───────────────────────────────────────────────
hero = '''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="280" viewBox="0 0 920 280">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#121820"/>
      <stop offset="55%" stop-color="#161C24"/>
      <stop offset="100%" stop-color="#1A222C"/>
    </linearGradient>
    <radialGradient id="glow1" cx="50%" cy="50%">
      <stop offset="0%" stop-color="#E07A5F" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#E07A5F" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="50%" cy="50%">
      <stop offset="0%" stop-color="#81B29A" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#81B29A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow3" cx="50%" cy="50%">
      <stop offset="0%" stop-color="#C9A227" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#C9A227" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#E07A5F"/>
      <stop offset="50%" stop-color="#C9A227"/>
      <stop offset="100%" stop-color="#81B29A" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="badge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#E07A5F" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#E07A5F" stop-opacity="0.08"/>
    </linearGradient>
  </defs>

  <rect width="920" height="280" rx="18" fill="url(#bg)"/>
  <rect x="1" y="1" width="918" height="278" rx="17" fill="none" stroke="#2A3340" stroke-width="1"/>

  <!-- ambient light -->
  <ellipse cx="780" cy="50" rx="200" ry="130" fill="url(#glow1)"/>
  <ellipse cx="120" cy="240" rx="180" ry="110" fill="url(#glow2)"/>
  <ellipse cx="500" cy="20" rx="260" ry="80" fill="url(#glow3)"/>

  <!-- grid ticks (technical feel) -->
  <g stroke="#2A3340" stroke-width="1" opacity="0.9">
    <line x1="40" y1="24" x2="120" y2="24"/>
    <line x1="40" y1="30" x2="90" y2="30"/>
    <line x1="800" y1="248" x2="880" y2="248"/>
    <line x1="830" y1="254" x2="880" y2="254"/>
  </g>

  <!-- constellation marks -->
  <g fill="none" stroke-linecap="round">
    <circle cx="820" cy="64" r="26" stroke="#81B29A" stroke-width="1.2" opacity="0.55"/>
    <circle cx="820" cy="64" r="10" stroke="#E07A5F" stroke-width="1.4" opacity="0.7"/>
    <circle cx="820" cy="64" r="3.5" fill="#E07A5F"/>
    <path d="M760 120 L 790 150 L 760 180 L 730 150 Z" stroke="#C9A227" stroke-width="1.2" opacity="0.45"/>
    <path d="M860 140 C 880 128, 892 156, 908 142" stroke="#E07A5F" stroke-width="1.5" opacity="0.5"/>
    <path d="M48 220 C 90 200, 130 240, 180 218 S 260 200, 300 220" stroke="#E07A5F" stroke-width="1.4" opacity="0.35" fill="none"/>
    <path d="M56 230 C 100 212, 140 248, 190 228 S 270 212, 310 230" stroke="#C9A227" stroke-width="1" opacity="0.22" fill="none"/>
  </g>

  <!-- brush / pen -->
  <g transform="translate(680,175) rotate(-18)" opacity="0.7">
    <rect x="0" y="-10" width="36" height="10" rx="2" fill="#E07A5F"/>
    <path d="M36 -10 L 52 -5 L 36 0 Z" fill="#C9A227"/>
    <rect x="6" y="-8" width="22" height="3" rx="1" fill="#F3EFE7" opacity="0.35"/>
  </g>

  <!-- overline -->
  <text x="48" y="52" font-family="Georgia, 'Times New Roman', serif" font-size="12" fill="#8B949E" letter-spacing="4">PORTFOLIO  ·  2026</text>

  <!-- name -->
  <text x="46" y="118" font-family="Georgia, 'Times New Roman', serif" font-size="64" fill="#F3EFE7" letter-spacing="-1.8">Ausartal</text>

  <!-- gradient rule -->
  <rect x="48" y="132" width="320" height="3" rx="1.5" fill="url(#rule)"/>

  <!-- tagline -->
  <text x="50" y="172" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="20" fill="#C8C0B4">Creating is drawing, erasing, and drawing again.</text>

  <!-- badges -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="#F3EFE7">
    <rect x="50" y="196" width="148" height="32" rx="16" fill="url(#badge)" stroke="#E07A5F" stroke-width="1"/>
    <text x="124" y="217" text-anchor="middle" fill="#E07A5F">GAME DEV · 6 YRS</text>

    <rect x="210" y="196" width="148" height="32" rx="16" fill="#C9A227" fill-opacity="0.12" stroke="#C9A227" stroke-width="1"/>
    <text x="284" y="217" text-anchor="middle" fill="#C9A227">DESIGN · 4 YRS</text>

    <rect x="370" y="196" width="132" height="32" rx="16" fill="#81B29A" fill-opacity="0.12" stroke="#81B29A" stroke-width="1"/>
    <text x="436" y="217" text-anchor="middle" fill="#81B29A">CODE · 5 YRS</text>

    <rect x="514" y="196" width="128" height="32" rx="16" fill="#B7B0A4" fill-opacity="0.1" stroke="#B7B0A4" stroke-width="1"/>
    <text x="578" y="217" text-anchor="middle" fill="#B7B0A4">SOUND · 1 YR</text>
  </g>

  <!-- corner brackets -->
  <path d="M20 50 L 20 20 L 50 20" stroke="#E07A5F" stroke-width="1.5" opacity="0.35" fill="none"/>
  <path d="M900 230 L 900 260 L 870 260" stroke="#81B29A" stroke-width="1.5" opacity="0.35" fill="none"/>
</svg>'''

# ─── 2. PRACTICE / TIMELINE ────────────────────────────────
practice = '''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="320" viewBox="0 0 400 320">
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#151C24"/>
      <stop offset="100%" stop-color="#111820"/>
    </linearGradient>
    <linearGradient id="b1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#E07A5F"/><stop offset="100%" stop-color="#E07A5F" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="b2" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#C9A227"/><stop offset="100%" stop-color="#C9A227" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="b3" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#81B29A"/><stop offset="100%" stop-color="#81B29A" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="b4" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#B7B0A4"/><stop offset="100%" stop-color="#B7B0A4" stop-opacity="0.2"/>
    </linearGradient>
    <radialGradient id="pg" cx="80%" cy="10%">
      <stop offset="0%" stop-color="#E07A5F" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#E07A5F" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="400" height="320" rx="16" fill="url(#panel)"/>
  <rect x="0.5" y="0.5" width="399" height="319" rx="15.5" fill="none" stroke="#2A3340"/>
  <rect width="400" height="320" rx="16" fill="url(#pg)"/>

  <text x="28" y="42" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="#6E7681" letter-spacing="3">YEARS OF PRACTICE</text>
  <rect x="28" y="54" width="72" height="2" rx="1" fill="#E07A5F"/>

  <!-- rows -->
  <text x="28" y="96" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="#F3EFE7">Game Development</text>
  <text x="360" y="96" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="#E07A5F" text-anchor="end">6</text>
  <rect x="28" y="108" width="332" height="8" rx="4" fill="#243040"/>
  <rect x="28" y="108" width="332" height="8" rx="4" fill="url(#b1)"/>

  <text x="28" y="152" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="#F3EFE7">Illustration &amp; Design</text>
  <text x="360" y="152" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="#C9A227" text-anchor="end">4</text>
  <rect x="28" y="164" width="332" height="8" rx="4" fill="#243040"/>
  <rect x="28" y="164" width="221" height="8" rx="4" fill="url(#b2)"/>

  <text x="28" y="208" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="#F3EFE7">Code &amp; Engineering</text>
  <text x="360" y="208" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="#81B29A" text-anchor="end">5</text>
  <rect x="28" y="220" width="332" height="8" rx="4" fill="#243040"/>
  <rect x="28" y="220" width="276" height="8" rx="4" fill="url(#b3)"/>

  <text x="28" y="264" font-family="Georgia, 'Times New Roman', serif" font-size="15" fill="#F3EFE7">Music &amp; Sound</text>
  <text x="360" y="264" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="#B7B0A4" text-anchor="end">1</text>
  <rect x="28" y="276" width="332" height="8" rx="4" fill="#243040"/>
  <rect x="28" y="276" width="62" height="8" rx="4" fill="url(#b4)"/>

  <!-- ticks -->
  <circle cx="372" cy="42" r="3" fill="#E07A5F" opacity="0.6"/>
  <circle cx="372" cy="52" r="3" fill="#81B29A" opacity="0.45"/>
</svg>'''

# ─── 3. STACK CHIPS ────────────────────────────────────────
stack = '''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="200" viewBox="0 0 560 200">
  <defs>
    <linearGradient id="sp" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#141B23"/><stop offset="100%" stop-color="#10161D"/>
    </linearGradient>
  </defs>
  <rect width="560" height="200" rx="14" fill="url(#sp)"/>
  <rect x="0.5" y="0.5" width="559" height="199" rx="13.5" fill="none" stroke="#2A3340"/>

  <text x="24" y="34" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="#6E7681" letter-spacing="2.5">CORE MATERIALS</text>

  <!-- row 1 -->
  <g font-family="Georgia, 'Times New Roman', serif" font-size="13">
    <rect x="24" y="50" width="100" height="32" rx="16" fill="#E07A5F" fill-opacity="0.12" stroke="#E07A5F"/>
    <text x="74" y="71" text-anchor="middle" fill="#E07A5F">Unreal</text>

    <rect x="134" y="50" width="92" height="32" rx="16" fill="#C9A227" fill-opacity="0.12" stroke="#C9A227"/>
    <text x="180" y="71" text-anchor="middle" fill="#C9A227">Godot 4</text>

    <rect x="236" y="50" width="92" height="32" rx="16" fill="#81B29A" fill-opacity="0.12" stroke="#81B29A"/>
    <text x="282" y="71" text-anchor="middle" fill="#81B29A">Unity</text>

    <rect x="338" y="50" width="120" height="32" rx="16" fill="#B7B0A4" fill-opacity="0.1" stroke="#B7B0A4"/>
    <text x="398" y="71" text-anchor="middle" fill="#B7B0A4">Pixel Game Maker</text>

    <rect x="468" y="50" width="68" height="32" rx="16" fill="#E07A5F" fill-opacity="0.1" stroke="#E07A5F" stroke-opacity="0.6"/>
    <text x="502" y="71" text-anchor="middle" fill="#E07A5F">Roblox</text>
  </g>

  <!-- row 2 -->
  <g font-family="Georgia, 'Times New Roman', serif" font-size="13">
    <rect x="24" y="96" width="88" height="32" rx="16" fill="#C9A227" fill-opacity="0.12" stroke="#C9A227"/>
    <text x="68" y="117" text-anchor="middle" fill="#C9A227">Figma</text>

    <rect x="122" y="96" width="88" height="32" rx="16" fill="#81B29A" fill-opacity="0.12" stroke="#81B29A"/>
    <text x="166" y="117" text-anchor="middle" fill="#81B29A">Maya</text>

    <rect x="220" y="96" width="96" height="32" rx="16" fill="#B7B0A4" fill-opacity="0.1" stroke="#B7B0A4"/>
    <text x="268" y="117" text-anchor="middle" fill="#B7B0A4">Adobe</text>

    <rect x="326" y="96" width="120" height="32" rx="16" fill="#E07A5F" fill-opacity="0.12" stroke="#E07A5F"/>
    <text x="386" y="117" text-anchor="middle" fill="#E07A5F">Clip Studio</text>

    <rect x="456" y="96" width="80" height="32" rx="16" fill="#C9A227" fill-opacity="0.1" stroke="#C9A227" stroke-opacity="0.6"/>
    <text x="496" y="117" text-anchor="middle" fill="#C9A227">Photoshop</text>
  </g>

  <!-- row 3 -->
  <g font-family="Georgia, 'Times New Roman', serif" font-size="13">
    <rect x="24" y="142" width="64" height="32" rx="16" fill="#81B29A" fill-opacity="0.12" stroke="#81B29A"/>
    <text x="56" y="163" text-anchor="middle" fill="#81B29A">C / C++</text>

    <rect x="98" y="142" width="64" height="32" rx="16" fill="#E07A5F" fill-opacity="0.12" stroke="#E07A5F"/>
    <text x="130" y="163" text-anchor="middle" fill="#E07A5F">C#</text>

    <rect x="172" y="142" width="72" height="32" rx="16" fill="#C9A227" fill-opacity="0.12" stroke="#C9A227"/>
    <text x="208" y="163" text-anchor="middle" fill="#C9A227">Python</text>

    <rect x="254" y="142" width="64" height="32" rx="16" fill="#B7B0A4" fill-opacity="0.1" stroke="#B7B0A4"/>
    <text x="286" y="163" text-anchor="middle" fill="#B7B0A4">Java</text>

    <rect x="328" y="142" width="96" height="32" rx="16" fill="#81B29A" fill-opacity="0.1" stroke="#81B29A" stroke-opacity="0.7"/>
    <text x="376" y="163" text-anchor="middle" fill="#81B29A">TypeScript</text>

    <rect x="434" y="142" width="92" height="32" rx="16" fill="#E07A5F" fill-opacity="0.1" stroke="#E07A5F" stroke-opacity="0.55"/>
    <text x="480" y="163" text-anchor="middle" fill="#E07A5F">FL Studio</text>
  </g>
</svg>'''

# ─── 4. FIGURES (hero numbers) ────────────────────────────
figures = '''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="200" viewBox="0 0 920 200">
  <defs>
    <linearGradient id="fg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#151C24"/><stop offset="100%" stop-color="#121920"/>
    </linearGradient>
    <radialGradient id="g1"><stop offset="0%" stop-color="#E07A5F" stop-opacity="0.16"/><stop offset="100%" stop-color="#E07A5F" stop-opacity="0"/></radialGradient>
    <radialGradient id="g2"><stop offset="0%" stop-color="#C9A227" stop-opacity="0.14"/><stop offset="100%" stop-color="#C9A227" stop-opacity="0"/></radialGradient>
    <radialGradient id="g3"><stop offset="0%" stop-color="#81B29A" stop-opacity="0.14"/><stop offset="100%" stop-color="#81B29A" stop-opacity="0"/></radialGradient>
    <radialGradient id="g4"><stop offset="0%" stop-color="#B7B0A4" stop-opacity="0.1"/><stop offset="100%" stop-color="#B7B0A4" stop-opacity="0"/></radialGradient>
  </defs>

  <rect width="920" height="200" rx="16" fill="url(#fg)"/>
  <rect x="0.5" y="0.5" width="919" height="199" rx="15.5" fill="none" stroke="#2A3340"/>

  <ellipse cx="130" cy="110" rx="120" ry="80" fill="url(#g1)"/>
  <ellipse cx="350" cy="110" rx="120" ry="80" fill="url(#g2)"/>
  <ellipse cx="570" cy="110" rx="120" ry="80" fill="url(#g3)"/>
  <ellipse cx="790" cy="110" rx="120" ry="80" fill="url(#g4)"/>

  <text x="36" y="38" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="#6E7681" letter-spacing="3">SELECTED FIGURES</text>
  <rect x="36" y="50" width="88" height="2" rx="1" fill="#E07A5F"/>

  <!-- 06 -->
  <text x="36" y="118" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="#E07A5F">06</text>
  <text x="36" y="148" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="#F3EFE7">years making games</text>
  <text x="36" y="170" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="#6E7681" letter-spacing="1.6">UNREAL · GODOT · UNITY · RBLX</text>

  <line x1="230" y1="70" x2="230" y2="170" stroke="#2A3340"/>

  <!-- 04 -->
  <text x="270" y="118" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="#C9A227">04</text>
  <text x="270" y="148" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="#F3EFE7">years designing</text>
  <text x="270" y="170" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="#6E7681" letter-spacing="1.6">FIGMA · MAYA · ADOBE · CSP</text>

  <line x1="470" y1="70" x2="470" y2="170" stroke="#2A3340"/>

  <!-- 05 -->
  <text x="510" y="118" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="#81B29A">05</text>
  <text x="510" y="148" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="#F3EFE7">years writing code</text>
  <text x="510" y="170" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="#6E7681" letter-spacing="1.6">C · C++ · C# · PYTHON · TS</text>

  <line x1="710" y1="70" x2="710" y2="170" stroke="#2A3340"/>

  <!-- 01 -->
  <text x="750" y="118" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="#B7B0A4">01</text>
  <text x="750" y="148" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="#F3EFE7">year scoring sound</text>
  <text x="750" y="170" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="#6E7681" letter-spacing="1.6">FL STUDIO · CAKEWALK</text>
</svg>'''

# ─── 5. FOOTER MARK ────────────────────────────────────────
footer = '''<svg xmlns="http://www.w3.org/2000/svg" width="180" height="40" viewBox="0 0 180 40">
  <path d="M20 26 C 50 8, 80 32, 110 14 S 150 8, 170 22" stroke="#E07A5F" stroke-width="1.5" stroke-linecap="round" opacity="0.55" fill="none"/>
  <circle cx="20" cy="26" r="2.5" fill="#C9A227" opacity="0.7"/>
  <circle cx="110" cy="14" r="2.5" fill="#81B29A" opacity="0.75"/>
  <circle cx="170" cy="22" r="2.5" fill="#E07A5F" opacity="0.7"/>
</svg>'''

# ─── 6. ACHIEVEMENT HUNTER PANEL ───────────────────────────
hunter = '''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="160" viewBox="0 0 920 160">
  <defs>
    <linearGradient id="hp" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#161C26"/><stop offset="100%" stop-color="#121820"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#C9A227"/><stop offset="100%" stop-color="#E07A5F"/>
    </linearGradient>
  </defs>
  <rect width="920" height="160" rx="16" fill="url(#hp)"/>
  <rect x="0.5" y="0.5" width="919" height="159" rx="15.5" fill="none" stroke="#2A3340"/>

  <!-- left icon -->
  <g transform="translate(48,50)">
    <circle cx="30" cy="30" r="28" stroke="#C9A227" stroke-width="1.5" fill="#C9A227" fill-opacity="0.12"/>
    <path d="M30 12 L 35 24 L 48 25 L 38 34 L 41 47 L 30 40 L 19 47 L 22 34 L 12 25 L 25 24 Z" fill="url(#gold)" opacity="0.9"/>
  </g>

  <text x="130" y="58" font-family="Georgia, 'Times New Roman', serif" font-size="22" fill="#F3EFE7">Achievement Hunter</text>
  <text x="130" y="86" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="#8B949E">Earning badges through real contribution — PRs, reviews, releases, and more.</text>
  <text x="130" y="118" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="#C9A227" letter-spacing="1.5">PULL SHARK  ·  QUICKDRAW  ·  YOLO  ·  STARSTRUCK  ·  GALAXY BRAIN</text>

  <!-- side marks -->
  <g opacity="0.5">
    <rect x="820" y="40" width="60" height="8" rx="4" fill="#E07A5F"/>
    <rect x="820" y="58" width="48" height="8" rx="4" fill="#C9A227"/>
    <rect x="820" y="76" width="54" height="8" rx="4" fill="#81B29A"/>
    <rect x="820" y="94" width="36" height="8" rx="4" fill="#B7B0A4"/>
  </g>
</svg>'''

jobs = {
    "hero.svg": hero,
    "practice.svg": practice,
    "stack.svg": stack,
    "figures.svg": figures,
    "footer.svg": footer,
    "hunter.svg": hunter,
}

for name, svg in jobs.items():
    svg_path = OUT / name
    png_path = OUT / name.replace(".svg", ".png")
    svg_path.write_text(svg, encoding="utf-8")
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(png_path), output_width=920 if name != "practice.svg" else 800, output_height=None)
    print(f"{name}: svg+xml  png={png_path.stat().st_size}b")

print("done")
