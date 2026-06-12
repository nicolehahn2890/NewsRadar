---
name: webdesign
description: Design und Code-Änderungen an der NewsRadar-Webseite (index.html). Verwenden, wenn Nicole das Aussehen, Layout, Farben oder Funktionen der Web-App ändern möchte oder Bugs vermutet.
---

# NewsRadar Webseite — Design & Änderungen

Die ganze App ist eine einzige Datei: `index.html` im Repository-Root.
Sie lädt `newsletter_latest.json` und zeigt die News an. Gehostet über
GitHub Pages, gelesen wird **ausschließlich vom `main`-Branch**.

## Design-System (Stand: Glow-up Juni 2026, von Nicole abgenommen)

- **Farben** (CSS-Variablen in `:root`): Hintergrund `#0a0f1a`/`#111827`,
  Akzent-Rosé `#c98878`, Rex-Grün `#4ab880`, Sektionsfarben:
  KI = Lila `#a78bfa`, Unternehmen = Blau `#60a5fa`, Börse = Gold `#fbbf24`.
- **Schriften:** Playfair Display (Überschriften/Logo), DM Sans (Fließtext),
  via Google Fonts.
- **Markenelemente:** Pixel-Rex im Header (SVG, viewBox 0 0 19 18, identisch
  mit dem App-Icon — siehe Skill `icon`) mit Radar-Ping-Animation und
  Bob-Animation; dunkle Karten mit 3px-Akzentlinie links, Glow-Punkt neben
  der Quelle, dezenter Farbschimmer oben rechts pro Karte.
- **Features:** Quellen-Filter-Chips, grünes "Heute"-Badge bei Artikeln vom
  aktuellen Tag, Skeleton-Shimmer beim Laden, "Stand:"-Zeile im Footer,
  `prefers-reduced-motion` wird respektiert.
- `<meta name="theme-color" content="#0a0f1a">` hält die Safari-Leiste dunkel.

## Stilregeln

- Eleganter, dunkler Look beibehalten — kein grelles Redesign.
- Mobile first: Nicole nutzt die Seite auf dem iPhone (Safari), max-width 720px.
- Alle Texte der Oberfläche auf Deutsch.
- **Kein** `apple-mobile-web-app-capable` / Standalone-Modus einbauen
  (Nicole will normales Safari-Verhalten; separater Speicher wäre die Folge).
- Story-Daten kommen NUR aus `newsletter_latest.json` — Struktur der Felder
  (`titel`, `text`, `quelle`, `datum_artikel`, `unternehmen`) nicht ändern,
  die schreibt der tägliche News-Agent (siehe CLAUDE.md).

## Bekannte Stolperfallen (bereits gefixt — nicht wieder einbauen)

- Datums-Strings IMMER mit `iso + 'T00:00:00'` parsen (siehe `formatDate`),
  sonst verrutscht das Datum je nach Zeitzone um einen Tag.
- Texte immer durch `escapeHtml()` schicken, bevor sie in `innerHTML` landen.
- JSON-Fetch mit Cache-Buster `?v=' + Date.now()` lassen, sonst zeigt
  Safari alte News.

## Testen vor dem Push (Pflicht)

In dieser Umgebung gibt es **keinen Browser/Screenshots** (Download von
Headless-Browsern ist von der Netzwerk-Policy gesperrt, `pip`/`npm` gehen).
Stattdessen:

1. JS-Syntax: `<script>`-Block extrahieren und `node --check` laufen lassen.
2. Funktionstest mit jsdom (`npm install jsdom` in /tmp): `index.html` laden,
   `fetch` mit der echten `newsletter_latest.json` stubben, dann prüfen:
   Datum-Badge, Filter-Chips, Anzahl Story-Karten pro Section, Klick auf
   einen Quellen-Chip filtert korrekt.
3. `python3 -c "import json; json.load(open('newsletter_latest.json'))"`.

## Veröffentlichen

- Direkt auf `main` committen und pushen (NIEMALS Branch/PR — siehe CLAUDE.md).
- Wenn der Push abgelehnt wird ("fetch first"): der tägliche News-Agent hat
  parallel gepusht → `git fetch origin main && git rebase origin/main`,
  dann erneut pushen.
- Nach dem Push `git log origin/main -1` prüfen.
- Nicole das Ergebnis in einfachen Worten beschreiben (sie ist keine
  Entwicklerin) und an den Link erinnern:
  https://nicolehahn2890.github.io/NewsRadar/
