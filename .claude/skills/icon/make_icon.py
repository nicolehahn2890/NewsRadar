import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

S = 180   # final icon size
SS = 4
B = S * SS

# ---- background: deep navy (#0b1020) + Liquid-Glass aura tints + ONE ring ----
# Passend zum neuen Glass-Design der Webseite: dunkles Navy mit dezentem
# Violett/Teal/Pink-Schimmer (wie die Aura im Hintergrund der App), dahinter
# ein grüner Halo, der den grünen Rex strahlen lässt.
bg = Image.new("RGB", (B, B), (11, 16, 32))   # #0b1020
d = ImageDraw.Draw(bg)
for y in range(B):
    t = y / B
    d.line([(0, y), (B, y)], fill=(int(11 + 9 * t), int(16 + 11 * t), int(32 + 16 * t)))

# Mehrfarbige Aura-Tints (sehr dezent, additiv) — Marken-Violett oben links,
# Teal unten rechts, ein Hauch Pink, plus grüner Halo hinter dem Rex.
def soft_glow(cx_f, cy_f, rad_f, color, blur_f=0.16):
    g = Image.new("RGB", (B, B), (0, 0, 0))
    gd = ImageDraw.Draw(g)
    gd.ellipse([B * (cx_f - rad_f), B * (cy_f - rad_f),
                B * (cx_f + rad_f), B * (cy_f + rad_f)], fill=color)
    return g.filter(ImageFilter.GaussianBlur(B * blur_f))

bg = ImageChops.add(bg, soft_glow(0.18, 0.16, 0.42, (30, 24, 60)))   # violet  #8b7cf0
bg = ImageChops.add(bg, soft_glow(0.86, 0.88, 0.40, (8, 36, 42)))    # teal    #2bb6c4
bg = ImageChops.add(bg, soft_glow(0.88, 0.16, 0.34, (40, 18, 32)))   # pink    #ffb0d2
bg = ImageChops.add(bg, soft_glow(0.50, 0.52, 0.40, (10, 34, 24), 0.12))  # green halo

d = ImageDraw.Draw(bg)
cx = cy = B // 2
r = int(B * 0.44)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(96, 86, 168), width=SS)  # violet ring #8b7cf0

icon = bg.resize((S, S), Image.LANCZOS)

# ---- big clear pixel T-Rex (chrome-dino style, facing right) ----
G = (52, 192, 138)    # body green  #34c08a
W = (255, 255, 255)   # eye + teeth
rows = [
    ".........GGGGGGGGGG",  # r0  head top
    "........GGWGGGGGGGG",  # r1  eye
    "........GGGGGGGGGGG",  # r2  upper jaw / snout
    "........GGGG.W.W...",  # r3  open mouth with teeth
    "........GGGGGGGGG..",  # r4  lower jaw
    "........GGGG.......",  # r5  neck
    "G......GGGGG.......",  # r6  tail tip
    "GG....GGGGGGG......",  # r7
    "GGG..GGGGGGGGG.....",  # r8
    "GGGGGGGGGGGGGGGG...",  # r9  tiny arm sticking out
    ".GGGGGGGGGGGG..G...",  # r10 little hand pointing down
    "..GGGGGGGGGG.......",  # r11
    "...GGGGGGGGG.......",  # r12
    "....GGGGGGG........",  # r13
    ".....GG..GG........",  # r14 legs
    ".....GG..GG........",  # r15
    ".....GG..GG........",  # r16
    ".....GGG..GGG......",  # r17 feet
]
COLS = max(len(r) for r in rows)
ROWS = len(rows)
SC = 8
ox = (S - COLS * SC) // 2
oy = (S - ROWS * SC) // 2

idr = ImageDraw.Draw(icon)
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch == ".":
            continue
        col = G if ch == "G" else W
        idr.rectangle([ox + x * SC, oy + y * SC,
                       ox + (x + 1) * SC - 1, oy + (y + 1) * SC - 1], fill=col)

icon.save(os.path.join(REPO_ROOT, "apple-touch-icon.png"), optimize=True)
icon.resize((540, 540), Image.NEAREST).save("/tmp/icon_preview2.png")

# SVG-Rechtecke für den Seitenkopf in index.html ausgeben (gleicher Rex!)
# Wenn sich das rows-Raster ändert, diese Ausgabe in das <svg class="rex-dino">
# in index.html übernehmen (viewBox="0 0 19 18").
print("\nSVG-Rects für index.html:")
for y, row in enumerate(rows):
    x = 0
    while x < len(row):
        if row[x] == ".":
            x += 1
            continue
        x2 = x
        while x2 < len(row) and row[x2] == row[x]:
            x2 += 1
        color = "#34c08a" if row[x] == "G" else "#fff"
        print(f'<rect x="{x}" y="{y}" width="{x2 - x}" height="1" fill="{color}"/>')
        x = x2
print("done")
