import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

S = 180   # final icon size
SS = 4
B = S * SS

# ---- background: dunkles, sattes Lila + Liquid-Glass-Schimmer + ONE ring ----
# Mittel-dunkles Violett, damit sich der grüne Rex klar absetzt. Sanfter
# Verlauf von etwas hellerem Violett oben zu tieferem Lila unten, dazu dezente
# Schimmer (Violett, Magenta, Blau-Violett) wie die Aura der App.
bg = Image.new("RGB", (B, B), (66, 48, 128))   # sattes Violett #423080
d = ImageDraw.Draw(bg)
for y in range(B):
    t = y / B
    d.line([(0, y), (B, y)], fill=(int(66 - 26 * t), int(48 - 20 * t), int(128 - 44 * t)))

# Farbige Aura-Tints per Alpha-Komposit — heben den dunklen Lila-Grund an,
# ohne ihn auszubleichen (Rex bleibt klar abgesetzt).
def soft_glow(base, cx_f, cy_f, rad_f, color, alpha, blur_f=0.18):
    mask = Image.new("L", (B, B), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([B * (cx_f - rad_f), B * (cy_f - rad_f),
                B * (cx_f + rad_f), B * (cy_f + rad_f)], fill=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(B * blur_f))
    layer = Image.new("RGB", (B, B), color)
    return Image.composite(layer, base, mask)

bg = soft_glow(bg, 0.16, 0.14, 0.46, (132, 102, 226), 120)  # helleres Violett oben links
bg = soft_glow(bg, 0.88, 0.18, 0.36, (160, 86, 184), 85)    # Magenta oben rechts
bg = soft_glow(bg, 0.14, 0.90, 0.40, (104, 118, 228), 80)   # Blau-Violett unten links
bg = soft_glow(bg, 0.88, 0.90, 0.40, (120, 88, 214), 100)   # Violett unten rechts

d = ImageDraw.Draw(bg)
cx = cy = B // 2
r = int(B * 0.44)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(176, 154, 255), width=SS)  # heller Violett-Ring

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
