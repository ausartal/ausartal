import cairosvg
from pathlib import Path

OUT = Path(r"C:\Users\ahmad\Documents\College\Subjects\Data Mining\github-profile\assets")

# Fluid illustrator pastels — washes, curves, no card/star/bars language
INK = "#1A1F26"
PAPER = "#F7F2EB"
MUTED = "#8B8680"
CORAL = "#E8A598"
BUTTER = "#EBD9A8"
SAGE = "#A8C5A8"
LILAC = "#C4B5D4"
SKY = "#A8C5D4"

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="280" viewBox="0 0 920 280">
  <!-- paper -->
  <rect width="920" height="280" fill="{INK}"/>

  <!-- fluid pastel washes -->
  <path d="M0 200 C 120 140, 220 250, 360 180 S 520 120, 640 190 S 780 240, 920 170 L 920 280 L 0 280 Z" fill="{SAGE}" opacity="0.18"/>
  <path d="M0 230 C 140 190, 260 260, 400 210 S 580 160, 720 220 S 840 250, 920 210 L 920 280 L 0 280 Z" fill="{CORAL}" opacity="0.16"/>
  <ellipse cx="780" cy="70" rx="160" ry="90" fill="{BUTTER}" opacity="0.22"/>
  <ellipse cx="160" cy="60" rx="130" ry="80" fill="{LILAC}" opacity="0.18"/>
  <ellipse cx="520" cy="40" rx="200" ry="60" fill="{SKY}" opacity="0.14"/>

  <!-- flowing brush strokes -->
  <path d="M40 210 C 140 170, 240 230, 360 190 S 520 150, 660 200 S 820 230, 880 195" stroke="{CORAL}" stroke-width="3.2" stroke-linecap="round" fill="none" opacity="0.55"/>
  <path d="M55 228 C 160 195, 270 245, 390 210 S 550 175, 690 218 S 830 245, 875 215" stroke="{BUTTER}" stroke-width="1.8" stroke-linecap="round" fill="none" opacity="0.4"/>
  <path d="M30 190 C 120 155, 230 210, 350 170 S 510 135, 650 185 S 810 215, 900 180" stroke="{LILAC}" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.35"/>

  <!-- sketchy orbital marks -->
  <path d="M720 60 C 760 40, 800 80, 840 55" stroke="{SAGE}" stroke-width="1.6" stroke-linecap="round" fill="none" opacity="0.55"/>
  <circle cx="720" cy="60" r="3" fill="{CORAL}" opacity="0.7"/>
  <circle cx="840" cy="55" r="2.5" fill="{SAGE}" opacity="0.7"/>
  <path d="M90 100 C 130 85, 150 120, 190 100" stroke="{BUTTER}" stroke-width="1.5" stroke-linecap="round" fill="none" opacity="0.5"/>

  <!-- soft pencil diamond / stamp -->
  <path d="M800 130 L 835 165 L 800 200 L 765 165 Z" stroke="{CORAL}" stroke-width="1.4" fill="{CORAL}" fill-opacity="0.12" opacity="0.7"/>
  <path d="M70 155 L 95 180 L 70 205 L 45 180 Z" stroke="{SKY}" stroke-width="1.2" fill="{SKY}" fill-opacity="0.1" opacity="0.55"/>

  <!-- overline -->
  <text x="64" y="72" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{MUTED}" letter-spacing="3.5">ILLUSTRATION  ·  GAME  ·  DESIGN  ·  CODE</text>

  <!-- wordmark -->
  <text x="60" y="138" font-family="Georgia, 'Times New Roman', serif" font-size="58" fill="{PAPER}" letter-spacing="-1.4">Ausartal</text>

  <!-- flourish under name -->
  <path d="M64 152 C 140 168, 220 152, 300 158 S 420 168, 480 156" stroke="{CORAL}" stroke-width="2.2" stroke-linecap="round" fill="none" opacity="0.75"/>
  <path d="M70 162 C 150 175, 240 162, 330 168 S 450 176, 500 168" stroke="{BUTTER}" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.45"/>

  <!-- tagline -->
  <text x="64" y="196" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="18" fill="{MUTED}">Creating is drawing, erasing, and drawing again.</text>

  <!-- disciplines as soft chips -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">
    <rect x="64" y="220" width="124" height="28" rx="14" fill="{CORAL}" fill-opacity="0.2" stroke="{CORAL}" stroke-opacity="0.55"/>
    <text x="126" y="239" text-anchor="middle" fill="{CORAL}">GAME · 6 YRS</text>

    <rect x="200" y="220" width="124" height="28" rx="14" fill="{BUTTER}" fill-opacity="0.2" stroke="{BUTTER}" stroke-opacity="0.55"/>
    <text x="262" y="239" text-anchor="middle" fill="{BUTTER}">DESIGN · 4 YRS</text>

    <rect x="336" y="220" width="120" height="28" rx="14" fill="{SAGE}" fill-opacity="0.2" stroke="{SAGE}" stroke-opacity="0.55"/>
    <text x="396" y="239" text-anchor="middle" fill="{SAGE}">CODE · 5 YRS</text>

    <rect x="468" y="220" width="124" height="28" rx="14" fill="{LILAC}" fill-opacity="0.2" stroke="{LILAC}" stroke-opacity="0.55"/>
    <text x="530" y="239" text-anchor="middle" fill="{LILAC}">SOUND · 1 YR</text>
  </g>
</svg>'''

(OUT / "hero.svg").write_text(hero, encoding="utf-8")
cairosvg.svg2png(bytestring=hero.encode("utf-8"), write_to=str(OUT / "hero.png"), output_width=920)
print("hero ok", (OUT / "hero.png").stat().st_size)
