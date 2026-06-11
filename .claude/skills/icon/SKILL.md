---
name: icon
description: NewsRadar-App-Icon (Pixel-Rex) neu generieren oder anpassen. Verwenden, wenn Nicole das Homescreen-Icon, das Favicon oder den Rex ändern möchte (Farbe, Motiv, Hintergrund).
---

# NewsRadar App-Icon (Pixel-Rex)

Das Icon für den iPhone-Homescreen und das Favicon der Webseite. Es zeigt
einen großen, klar erkennbaren Pixel-T-Rex (Stil des Chrome-Dinos) auf
dunkelblauem Hintergrund mit einem dezenten Radar-Ring.

## So wird das Icon generiert

Das Skript `make_icon.py` in diesem Ordner erzeugt das Icon:

```
pip install pillow -q
python3 .claude/skills/icon/make_icon.py
```

Es schreibt `apple-touch-icon.png` (180×180 px) ins Repository-Root und
eine große Vorschau nach `/tmp/icon_preview2.png`.

## Design-Vorgaben (von Nicole abgenommen)

- Der Rex muss **groß und sofort erkennbar** sein — er füllt fast das ganze
  Icon. Keine kleinteiligen Details, keine vielen Ringe/Blips (das war die
  erste Version, die Nicole abgelehnt hat: "man erkennt nicht, was das ist").
- T-Rex-Merkmale: großer Kopf mit offenem Maul und weißen Zähnen, weißes
  Auge, winziges Ärmchen, kräftiger Schwanz, zwei Beine.
- Farben wie die Webseite: Hintergrund-Verlauf ab `#0a0f1a`, Rex in
  `#4ab880`, ein einzelner dezenter Ring in Blaugrau.
- Der Rex ist als Pixel-Raster im Skript definiert (`rows`-Liste:
  `G` = grün, `W` = weiß, `.` = leer) — Änderungen am Motiv dort machen.
- Keine Schrift im Icon. iOS rundet die Ecken selbst ab, also Quadrat
  voll ausnutzen, nichts Wichtiges in die Ecken.

## Nach jeder Änderung — Pflichtschritte

1. Vorschau selbst ansehen (Read auf `/tmp/icon_preview2.png`) und prüfen,
   dass der Rex klar erkennbar ist. Vorschau auch an Nicole schicken.
2. In `index.html` die Versionsnummer in beiden `<link>`-Tags hochzählen
   (`apple-touch-icon.png?v=2` → `?v=3` usw.), sonst zeigen iPhone und
   Browser das alte, zwischengespeicherte Icon.
3. Committen und **direkt auf `main` pushen** (niemals Branch/PR — siehe
   CLAUDE.md), danach mit `git log origin/main -1` prüfen.
4. Nicole in einfachen Worten erklären, dass sie das Symbol auf dem
   Homescreen einmal löschen und über Safari → Teilen →
   "Zum Home-Bildschirm" neu hinzufügen muss, damit das neue Bild erscheint.

## Wichtig: kein Web-App-Modus

**Niemals** `apple-mobile-web-app-capable` (Standalone-/Vollbild-Modus) in
`index.html` einbauen. Nicole will, dass die Seite normal in Safari öffnet
und alles funktioniert wie bisher; der Standalone-Modus würde außerdem einen
separaten Speicher (localStorage) verwenden.
