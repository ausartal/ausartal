"""Regenerate profile assets — editorial, monochrome, no glow/AI-slop."""
import cairosvg
from pathlib import Path

OUT = Path(r"C:\Users\ahmad\Documents\College\Subjects\Data Mining\github-profile\assets")
OUT.mkdir(parents=True, exist_ok=True)

# Palette: ink / paper / single muted accent (no neon, no rainbow, no glow)
INK = "#0D1117"
PANEL = "#161B22"
LINE = "#30363D"
MUTED = "#8B949E"
PAPER = "#E6EDF3"
ACCENT = "#B08968"  # muted clay — restrained, not terracotta-orange
ACCENT2 = "#6E7681"

# ─── HERO — flat, no radial glow ───────────────────────────
hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="260" viewBox="0 0 920 260">
  <rect width="920" height="260" rx="12" fill="{INK}"/>
  <rect x="0.5" y="0.5" width="919" height="259" rx="11.5" fill="none" stroke="{LINE}"/>

  <!-- thin top rule -->
  <rect x="48" y="40" width="64" height="1" fill="{ACCENT}"/>

  <text x="48" y="72" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{MUTED}" letter-spacing="3.5">PORTFOLIO</text>

  <text x="46" y="132" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="{PAPER}" letter-spacing="-1.2">Ausartal</text>

  <text x="48" y="172" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="18" fill="{MUTED}">Creating is drawing, erasing, and drawing again.</text>

  <!-- monochrome discipline labels -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{PAPER}">
    <rect x="48" y="198" width="128" height="30" rx="2" fill="none" stroke="{LINE}"/>
    <text x="112" y="218" text-anchor="middle" letter-spacing="1.2">GAME DEV · 6 YRS</text>

    <rect x="188" y="198" width="120" height="30" rx="2" fill="none" stroke="{LINE}"/>
    <text x="248" y="218" text-anchor="middle" letter-spacing="1.2">DESIGN · 4 YRS</text>

    <rect x="320" y="198" width="112" height="30" rx="2" fill="none" stroke="{LINE}"/>
    <text x="376" y="218" text-anchor="middle" letter-spacing="1.2">CODE · 5 YRS</text>

    <rect x="444" y="198" width="116" height="30" rx="2" fill="none" stroke="{LINE}"/>
    <text x="502" y="218" text-anchor="middle" letter-spacing="1.2">SOUND · 1 YR</text>
  </g>

  <!-- restrained geometric mark, right -->
  <g fill="none" stroke="{LINE}" stroke-width="1">
    <line x1="780" y1="80" x2="860" y2="80"/>
    <line x1="800" y1="100" x2="860" y2="100"/>
    <rect x="780" y="130" width="48" height="48" stroke="{ACCENT}" stroke-opacity="0.5"/>
    <line x1="780" y1="130" x2="828" y2="178" stroke="{ACCENT}" stroke-opacity="0.35"/>
  </g>
</svg>'''

# ─── PRACTICE bars — flat, grayscale + one accent ──────────
practice = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
  <rect width="400" height="300" rx="10" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="399" height="299" rx="9.5" fill="none" stroke="{LINE}"/>

  <text x="28" y="40" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2.5">YEARS OF PRACTICE</text>
  <rect x="28" y="50" width="48" height="1" fill="{ACCENT}"/>

  <!-- 6 -->
  <text x="28" y="92" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Game Development</text>
  <text x="360" y="92" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{PAPER}" text-anchor="end">6</text>
  <rect x="28" y="104" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="104" width="332" height="4" fill="{PAPER}"/>

  <!-- 4 -->
  <text x="28" y="146" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Illustration &amp; Design</text>
  <text x="360" y="146" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{PAPER}" text-anchor="end">4</text>
  <rect x="28" y="158" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="158" width="221" height="4" fill="{MUTED}"/>

  <!-- 5 -->
  <text x="28" y="200" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Code &amp; Engineering</text>
  <text x="360" y="200" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{PAPER}" text-anchor="end">5</text>
  <rect x="28" y="212" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="212" width="276" height="4" fill="{ACCENT}"/>

  <!-- 1 -->
  <text x="28" y="254" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="{PAPER}">Music &amp; Sound</text>
  <text x="360" y="254" font-family="Georgia, 'Times New Roman', serif" font-size="20" fill="{PAPER}" text-anchor="end">1</text>
  <rect x="28" y="266" width="332" height="4" fill="#21262D"/>
  <rect x="28" y="266" width="62" height="4" fill="{ACCENT2}"/>
</svg>'''

# ─── STACK — black/white capsules only ─────────────────────
stack = f'''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="190" viewBox="0 0 560 190">
  <rect width="560" height="190" rx="10" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="559" height="189" rx="9.5" fill="none" stroke="{LINE}"/>

  <text x="24" y="32" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2.5">CORE MATERIALS</text>
  <rect x="24" y="42" width="40" height="1" fill="{PAPER}" opacity="0.5"/>

  <!-- row 1: white outline on dark = black/white capsule -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{PAPER}">
    <rect x="24" y="58" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="68" y="76" text-anchor="middle">Unreal</text>

    <rect x="120" y="58" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="164" y="76" text-anchor="middle">Godot 4</text>

    <rect x="216" y="58" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="260" y="76" text-anchor="middle">Unity</text>

    <rect x="312" y="58" width="132" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="378" y="76" text-anchor="middle">Pixel Game Maker</text>

    <rect x="452" y="58" width="84" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="494" y="76" text-anchor="middle">Roblox</text>
  </g>

  <!-- row 2 -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{PAPER}">
    <rect x="24" y="98" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/>
    <text x="68" y="116" text-anchor="middle" fill="{MUTED}">Figma</text>

    <rect x="120" y="98" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/>
    <text x="164" y="116" text-anchor="middle" fill="{MUTED}">Maya</text>

    <rect x="216" y="98" width="88" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/>
    <text x="260" y="116" text-anchor="middle" fill="{MUTED}">Adobe</text>

    <rect x="312" y="98" width="112" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/>
    <text x="368" y="116" text-anchor="middle" fill="{MUTED}">Clip Studio</text>

    <rect x="432" y="98" width="104" height="28" rx="14" fill="{PAPER}" fill-opacity="0.08" stroke="{PAPER}" stroke-opacity="0.35"/>
    <text x="484" y="116" text-anchor="middle" fill="{MUTED}">Photoshop</text>
  </g>

  <!-- row 3 -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{PAPER}">
    <rect x="24" y="138" width="88" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="68" y="156" text-anchor="middle">C / C++</text>

    <rect x="120" y="138" width="64" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="152" y="156" text-anchor="middle">C#</text>

    <rect x="192" y="138" width="80" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="232" y="156" text-anchor="middle">Python</text>

    <rect x="280" y="138" width="64" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="312" y="156" text-anchor="middle">Java</text>

    <rect x="352" y="138" width="96" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="400" y="156" text-anchor="middle">TypeScript</text>

    <rect x="456" y="138" width="80" height="28" rx="14" fill="#0D1117" stroke="{PAPER}" stroke-opacity="0.55"/>
    <text x="496" y="156" text-anchor="middle">FL Studio</text>
  </g>
</svg>'''

# ─── FIGURES — flat, no glow ───────────────────────────────
figures = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="180" viewBox="0 0 920 180">
  <rect width="920" height="180" rx="10" fill="{INK}"/>
  <rect x="0.5" y="0.5" width="919" height="179" rx="9.5" fill="none" stroke="{LINE}"/>

  <text x="36" y="36" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="3">SELECTED FIGURES</text>
  <rect x="36" y="46" width="56" height="1" fill="{ACCENT}"/>

  <text x="36" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{PAPER}">06</text>
  <text x="36" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">years making games</text>
  <text x="36" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">UNREAL · GODOT · UNITY · RBLX</text>

  <line x1="230" y1="64" x2="230" y2="158" stroke="{LINE}"/>

  <text x="270" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{MUTED}">04</text>
  <text x="270" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">years designing</text>
  <text x="270" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">FIGMA · MAYA · ADOBE · CSP</text>

  <line x1="470" y1="64" x2="470" y2="158" stroke="{LINE}"/>

  <text x="510" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{ACCENT}">05</text>
  <text x="510" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">years writing code</text>
  <text x="510" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">C · C++ · C# · PYTHON · TS</text>

  <line x1="710" y1="64" x2="710" y2="158" stroke="{LINE}"/>

  <text x="750" y="110" font-family="Georgia, 'Times New Roman', serif" font-size="52" fill="{MUTED}">01</text>
  <text x="750" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">year scoring sound</text>
  <text x="750" y="158" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9" fill="{MUTED}" letter-spacing="1.4">FL STUDIO · CAKEWALK</text>
</svg>'''

jobs = {"hero.svg": hero, "practice.svg": practice, "stack.svg": stack, "figures.svg": figures}

for name, svg in jobs.items():
    (OUT / name).write_text(svg, encoding="utf-8")
    png = OUT / name.replace(".svg", ".png")
    w = 800 if name == "practice.svg" else 920
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(png), output_width=w)
    print(f"{name} → {png.name} {png.stat().st_size}b")

print("done")
