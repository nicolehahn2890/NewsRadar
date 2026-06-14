---
name: icon
description: NewsRadar-App-Icon (Pixel-Rex) neu generieren oder anpassen. Verwenden, wenn Nicole das Homescreen-Icon, das Favicon oder den Rex ändern möchte (Farbe, Motiv, Hintergrund).
---

# NewsRadar App-Icon (Pixel-Rex)

Das Icon für den iPhone-Homescreen und das Favicon der Webseite. Es zeigt
einen großen, klar erkennbaren Pixel-T-Rex (Stil des Chrome-Dinos) auf
einem satten, mittel-dunklen Lila-Hintergrund mit einem dezenten Radar-Ring
— passend zum Liquid-Glass-Design der Webseite.

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
- Farben wie die Webseite (Liquid-Glass-Design): Hintergrund ist ein
  sattes, mittel-dunkles Lila (Verlauf ab ca. `#423080`) mit dezentem
  Violett/Magenta/Blau-Schimmer; der Rex ist im neuen Grün `#34c08a`
  gehalten und hebt sich klar vom Lila ab; ein einzelner Ring in hellem
  Violett. Hinweis: zu hell darf das Lila NICHT werden, sonst verschwimmt
  der grüne Rex (von Nicole getestet und abgelehnt).
- Der Rex ist als Pixel-Raster im Skript definiert (`rows`-Liste:
  `G` = grün, `W` = weiß, `.` = leer) — Änderungen am Motiv dort machen.
- Keine Schrift im Icon. iOS rundet die Ecken selbst ab, also Quadrat
  voll ausnutzen, nichts Wichtiges in die Ecken.

## Der Rex steht an ZWEI Stellen

Derselbe Pixel-Rex existiert zweimal — bei Motiv-Änderungen **beide** anpassen:

1. `apple-touch-icon.png` — wird von `make_icon.py` erzeugt.
2. Das Inline-SVG `<svg class="rex-dino" viewBox="0 0 19 18">` im Header von
   `index.html` (mit animiertem Radar-Ping drumherum).

`make_icon.py` druckt nach dem Generieren die fertigen `<rect>`-Zeilen für
das SVG — diese einfach in `index.html` übernehmen.

## Nach jeder Änderung — Pflichtschritte

1. Vorschau selbst ansehen (Read auf `/tmp/icon_preview2.png`) und prüfen,
   dass der Rex klar erkennbar ist. Vorschau auch an Nicole schicken.
2. In `index.html` die Versionsnummer in beiden `<link>`-Tags hochzählen
   (aktuell `apple-touch-icon.png?v=5` → dann `?v=6` usw.), sonst zeigen
   iPhone und Browser das alte, zwischengespeicherte Icon.
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
