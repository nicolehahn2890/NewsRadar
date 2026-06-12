import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

S = 180   # final icon size
SS = 4
B = S * SS

# ---- background: dark navy gradient + soft green glow, ONE faint ring ----
bg = Image.new("RGB", (B, B), (10, 15, 26))
d = ImageDraw.Draw(bg)
for y in range(B):
    t = y / B
    d.line([(0, y), (B, y)], fill=(int(10 + 7 * t), int(15 + 9 * t), int(26 + 13 * t)))

glow = Image.new("RGB", (B, B), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([B * 0.12, B * 0.10, B * 0.88, B * 0.90], fill=(10, 30, 19))
glow = glow.filter(ImageFilter.GaussianBlur(B * 0.10))
bg = ImageChops.add(bg, glow)

d = ImageDraw.Draw(bg)
cx = cy = B // 2
r = int(B * 0.44)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(34, 52, 84), width=SS)

icon = bg.resize((S, S), Image.LANCZOS)

# ---- big clear pixel T-Rex (chrome-dino style, facing right) ----
G = (74, 184, 128)    # body green  #4ab880
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
        color = "#4ab880" if row[x] == "G" else "#fff"
        print(f'<rect x="{x}" y="{y}" width="{x2 - x}" height="1" fill="{color}"/>')
        x = x2
print("done")
