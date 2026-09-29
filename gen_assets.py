import cairosvg
from pathlib import Path

OUT = Path(r"C:\Users\ahmad\Documents\College\Subjects\Data Mining\github-profile\assets")

# Pastel, refined — illustrator studio, not AI neon
INK = "#121820"
PANEL = "#1A222B"
LINE = "#2F3A45"
MUTED = "#9AA5B1"
PAPER = "#F2EDE6"

# pastel accents
CORAL = "#E8A598"   # soft coral
BUTTER = "#E8D5A3"  # butter
SAGE = "#A8C5A8"    # sage
LILAC = "#B8A9C9"   # lilac
SKY = "#A8C0D4"     # dusty sky

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="230" viewBox="0 0 920 230">
  <!-- card -->
  <rect x="10" y="10" width="900" height="210" rx="18" fill="{PANEL}"/>
  <rect x="10.5" y="10.5" width="899" height="209" rx="17.5" fill="none" stroke="{LINE}"/>

  <!-- illustrator mark: nib / pen star hybrid -->
  <circle cx="78" cy="115" r="36" stroke="{CORAL}" stroke-width="1.8" fill="{CORAL}" fill-opacity="0.14"/>
  <path d="M78 88 L 84 108 L 105 109 L 89 122 L 94 142 L 78 129 L 62 142 L 67 122 L 51 109 L 72 108 Z" fill="{CORAL}" opacity="0.92"/>
  <!-- nib stroke under star -->
  <path d="M64 150 C 72 146, 84 154, 92 148" stroke="{BUTTER}" stroke-width="1.6" stroke-linecap="round" fill="none" opacity="0.75"/>

  <!-- overline -->
  <text x="140" y="58" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" fill="{MUTED}" letter-spacing="3.2">ILLUSTRATOR  ·  GAME  ·  DESIGN  ·  CODE</text>

  <!-- name -->
  <text x="138" y="112" font-family="Georgia, 'Times New Roman', serif" font-size="42" fill="{PAPER}" letter-spacing="-0.8">Ausartal</text>

  <!-- subtitle -->
  <text x="140" y="148" font-family="Georgia, 'Times New Roman', serif" font-size="16" fill="{MUTED}">Creating is drawing, erasing, and drawing again —</text>
  <text x="140" y="172" font-family="Georgia, 'Times New Roman', serif" font-size="16" fill="{MUTED}">illustration, game craft, and software, practiced for years.</text>

  <!-- badge line -->
  <text x="140" y="204" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" fill="{CORAL}" letter-spacing="1.15">GAME DEV  ·  DESIGN  ·  CODE  ·  SOUND</text>

  <!-- pastel accent bars -->
  <rect x="780" y="72" width="88" height="7" rx="3.5" fill="{CORAL}"/>
  <rect x="780" y="90" width="72" height="7" rx="3.5" fill="{BUTTER}"/>
  <rect x="780" y="108" width="82" height="7" rx="3.5" fill="{SAGE}"/>
  <rect x="780" y="126" width="58" height="7" rx="3.5" fill="{LILAC}"/>
  <rect x="780" y="144" width="68" height="7" rx="3.5" fill="{SKY}"/>

  <!-- soft corner ticks -->
  <path d="M28 36 L 28 22 L 42 22" stroke="{BUTTER}" stroke-width="1.2" opacity="0.4" fill="none"/>
  <path d="M892 194 L 892 208 L 878 208" stroke="{SAGE}" stroke-width="1.2" opacity="0.4" fill="none"/>
</svg>'''

# Practice panel used as full-width strip under Practice text (optional header art)
practice = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="120" viewBox="0 0 920 120">
  <rect x="10" y="10" width="900" height="100" rx="14" fill="{PANEL}"/>
  <rect x="10.5" y="10.5" width="899" height="99" rx="13.5" fill="none" stroke="{LINE}"/>

  <text x="36" y="42" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" fill="{MUTED}" letter-spacing="2.8">YEARS OF PRACTICE</text>

  <!-- pastel mini-bars full width -->
  <rect x="36" y="58" width="200" height="6" rx="3" fill="{CORAL}"/>
  <rect x="248" y="58" width="140" height="6" rx="3" fill="{BUTTER}"/>
  <rect x="400" y="58" width="175" height="6" rx="3" fill="{SAGE}"/>
  <rect x="587" y="58" width="40" height="6" rx="3" fill="{LILAC}"/>

  <text x="36" y="88" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{PAPER}">06 games</text>
  <text x="150" y="88" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{MUTED}">04 design</text>
  <text x="270" y="88" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{MUTED}">05 code</text>
  <text x="380" y="88" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="{MUTED}">01 sound</text>

  <rect x="800" y="36" width="64" height="6" rx="3" fill="{CORAL}" opacity="0.7"/>
  <rect x="800" y="52" width="52" height="6" rx="3" fill="{BUTTER}" opacity="0.7"/>
  <rect x="800" y="68" width="58" height="6" rx="3" fill="{SAGE}" opacity="0.7"/>
</svg>'''

for name, svg, w in [("hero.svg", hero, 920), ("practice.svg", practice, 920)]:
    (OUT / name).write_text(svg, encoding="utf-8")
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(OUT / name.replace(".svg", ".png")), output_width=w)
    print(name, "ok")
print("done")
