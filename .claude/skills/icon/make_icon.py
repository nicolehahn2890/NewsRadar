import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

S = 180   # final icon size
SS = 4
B = S * SS

# ---- background: helles Lavendel/Lila + Liquid-Glass-Schimmer + ONE ring ----
# Nach Nicoles Wunsch heller und lila-dominant — der grüne Rex hebt sich auf
# dem hellen Lila klar ab. Sanfter Verlauf von hellem Lavendel nach kräftigerem
# Violett unten, dazu dezente Schimmer (Violett, Pink, Blau) wie die Aura der App.
bg = Image.new("RGB", (B, B), (206, 198, 244))   # helles Lavendel #cec6f4
d = ImageDraw.Draw(bg)
for y in range(B):
    t = y / B
    d.line([(0, y), (B, y)], fill=(int(206 - 36 * t), int(198 - 40 * t), int(244 - 28 * t)))

# Farbige Aura-Tints — auf hellem Grund per Alpha-Komposit (nicht additiv,
# sonst würde der helle Hintergrund ausbleichen).
def soft_glow(base, cx_f, cy_f, rad_f, color, alpha, blur_f=0.18):
    mask = Image.new("L", (B, B), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([B * (cx_f - rad_f), B * (cy_f - rad_f),
                B * (cx_f + rad_f), B * (cy_f + rad_f)], fill=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(B * blur_f))
    layer = Image.new("RGB", (B, B), color)
    return Image.composite(layer, base, mask)

bg = soft_glow(bg, 0.16, 0.14, 0.46, (150, 120, 238), 130)  # Violett oben links
bg = soft_glow(bg, 0.88, 0.18, 0.38, (244, 180, 222), 95)   # Pink oben rechts
bg = soft_glow(bg, 0.14, 0.90, 0.40, (150, 180, 246), 90)   # Blau unten links
bg = soft_glow(bg, 0.88, 0.90, 0.40, (140, 110, 230), 115)  # Violett unten rechts

d = ImageDraw.Draw(bg)
cx = cy = B // 2
r = int(B * 0.44)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(124, 92, 240), width=SS)  # kräftiger Violett-Ring #7c5cf0

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
