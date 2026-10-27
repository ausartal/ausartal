"""Generate MiMo CLI-style meteor (shooting star) SVG fragment.

Design extracted from the MiMo TUI vivid-mode renderer (mimo.exe):
- head: 5-dot plus cluster (radius-1 mask over a 3x3 dot grid), white
- trail: uniform braille-sized dots behind the head, pale blue (180,215,255),
  quantized to a 2px grid like terminal braille subdots
- alpha falloff pow(1 - d/L, 1.3); color blends to white within 5/32 of trail
- trajectory: 0.36 rad (~20.6 deg) below horizontal, falling to lower-left
- life envelope sin(pi t/life); RV = 3600ms
"""
import math

ANGLE = 0.36
L = 190.0
STEP = 4.2
GRID = 2.0
LIFE = 3.6
BLEND = 5.0 / 32.0 * L
DOT_R = 1.6
TRAVEL = 320.0  # px covered per life cycle


def lerp(a, b, t):
    return a + (b - a) * t


def snap(v):
    return round(v / GRID) * GRID


def hexc(c):
    return "#%02X%02X%02X" % c


def meteor(begin, head_start, dur, scale=1.0):
    hx, hy = head_start
    mx, my = -math.cos(ANGLE), math.sin(ANGLE)   # motion: left-down
    tx, ty = -mx, -my                             # trail behind head: right-up
    r = DOT_R * scale

    # base transform parks the streak at its spawn pose (nice fallback
    # when SMIL is off); animateTransform takes over once it begins.
    p = [f'  <g opacity="1" transform="translate({hx:g} {hy:g})">']
    for dx, dy in ((0, 0), (3.2, 0), (-3.2, 0), (0, 3.2), (0, -3.2)):
        p.append(f'    <circle cx="{snap(dx * scale):g}" cy="{snap(dy * scale):g}" '
                 f'r="{r:.2f}" fill="#FFFFFF"/>')

    d = 4.6
    while d <= L:
        frac = d / L
        alpha = (1.0 - frac) ** 1.3 * 0.92
        if alpha < 0.04:
            break
        mix = max(0.0, 1.0 - d / BLEND)
        c = (round(lerp(180, 255, mix)),
             round(lerp(215, 255, mix)),
             round(lerp(255, 255, mix)))
        px, py = snap(tx * d * scale), snap(ty * d * scale)
        p.append(f'    <circle cx="{px:g}" cy="{py:g}" r="{r:.2f}" '
                 f'opacity="{alpha:.2f}" fill="{hexc(c)}"/>')
        d += STEP

    ex, ey = hx + mx * TRAVEL, hy + my * TRAVEL
    p.append(f'    <animateTransform attributeName="transform" type="translate" '
             f'values="{hx:g} {hy:g};{ex:.0f} {ey:.0f}" '
             f'dur="{dur}s" begin="{begin}" repeatCount="indefinite"/>')
    p.append(f'    <animate attributeName="opacity" values="0;1;1;0" '
             f'keyTimes="0;0.18;0.72;1" dur="{dur}s" begin="{begin}" '
             f'repeatCount="indefinite"/>')
    p.append("  </g>")
    return "\n".join(p)


if __name__ == "__main__":
    out = ["  <!-- shooting stars · MiMo CLI meteor style -->"]
    out.append(meteor("0s", (880, 42), LIFE, 1.0))
    out.append(meteor("1.4s", (1062, 178), LIFE, 0.8))
    out.append(meteor("2.8s", (456, 18), LIFE, 0.62))
    print("\n".join(out))
