---
name: webdesign
description: Design und Code-Änderungen an der NewsRadar-Webseite (index.html). Verwenden, wenn Nicole das Aussehen, Layout, Farben oder Funktionen der Web-App ändern möchte oder Bugs vermutet.
---

# NewsRadar Webseite — Design & Änderungen

Die ganze App ist eine einzige Datei: `index.html` im Repository-Root.
Sie lädt `newsletter_latest.json` und zeigt die News an. Gehostet über
GitHub Pages, gelesen wird **ausschließlich vom `main`-Branch**.

## Design-System (Stand: Liquid-Glass-Redesign Juni 2026, von Nicole abgenommen)

Das komplette Design steckt **inline im `<style>`-Block von `index.html`**
(die Design-Tokens + die `.nr-*`-Glass-Klassen). Vorlage war das von Nicole
mit Claude Design erstellte Paket „NewsRadar Design System (Liquid Glass)".

- **Zwei Themes**, umgeschaltet über `data-theme` am `<html>`-Tag:
  `light` (Standard) und `dark`. Die Auswahl wird in `localStorage`
  (`nr-theme`) gespeichert und schon im `<head>` per Inline-Script gesetzt,
  damit beim Laden nichts aufblitzt. `<meta name="theme-color">` wird per JS
  passend mitgeschaltet (`#eaf0f7` hell / `#0b1020` dunkel).
- **Marken-/Kategorie-Farben** (theme-unabhängige CSS-Variablen):
  `--nr-violet #8b7cf0` (Marke + KI-Branche), `--nr-blue #5b8def`
  (Unternehmen), `--nr-teal #2bb6c4` (Börse & Gold), `--nr-green #34c08a`
  (Rex + „Heute"/frisch). Hintergrund-Basis hell `#eaf0f7` / dunkel `#0b1020`.
- **Glas-Material:** durchscheinende Flächen mit `backdrop-filter: blur`,
  iridiszierender Rand (`--glass-bevel`) und farbigem Schlagschatten. Genutzt
  über die Utility-Klassen — Komponenten kombinieren sie statt eigenes CSS:
  - `.nr-glass` = Grund-Glasfläche; Radius-Varianten `--pill` / `--lg` / `--sm`.
  - `.nr-glass--frosted` = blickdichter (für textlastige Story-Karten, damit
    die langen deutschen Zusammenfassungen lesbar bleiben).
  - `.nr-glass--interactive` = Hover-Lift + Press-Scale (Chips).
  - `.nr-glass--sheen` + ein `<span class="nr-sheen"></span>` als erstes Kind
    = feiner Lichtschimmer an der Oberkante.
  - `.nr-glass--tint` (Farbglas, `--tint` inline) — aktuell ungenutzt, bereit.
- **Schriften:** Playfair Display (Logo, Section-Titel, Story-Überschriften),
  DM Sans (Fließtext) — per `@import` im `<style>`.
- **Markenelemente:** Wortmarke „News**Radar**", wobei „Radar" über
  `.nr-prism-text` einen Regenbogen-Verlauf trägt; Pixel-Rex im Header
  (SVG, viewBox 0 0 19 18, identisch mit dem App-Icon — siehe Skill `icon`,
  Farbe `#34c08a`) mit Radar-Ping (`.nr-radar`) und Bob-Animation; pro Section
  ein farbiges Glas-Icon-Chip (Lucide-Style-SVGs: sparkles / building / trending-up).
- **Features:** Hell/Dunkel-Umschalter (Glas-Segmented-Control oben),
  Quellen-Filter-Chips, grünes „Heute"-Badge bei Artikeln vom aktuellen Tag,
  Skeleton-Shimmer beim Laden, „Stand:"-Zeile im Footer,
  `prefers-reduced-motion` wird respektiert.

Die Original-Design-Referenz (`newsradar-glass.css`, `newsradar-glass-reference.html`,
README mit Mapping-Tabelle) lag im ZIP, das Nicole hochgeladen hat — sie ist
**nicht** im Repo eingecheckt. Die maßgebliche Umsetzung ist `index.html`.

## Stilregeln

- Eleganter Glas-Look beibehalten — kein grelles Redesign. Standard ist das
  **helle** Theme; Dunkel ist über den Umschalter erreichbar.
- Beide Themes immer mitdenken: Farben/Schatten über die `--glass-*`- und
  Text-Variablen lösen, nie hart kodieren, sonst bricht eines der Themes.
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

1. JS-Syntax: **beide** `<script>`-Blöcke extrahieren (das frühe Theme-Script
   im `<head>` + das App-Script am Ende) und je `node --check` laufen lassen.
2. Funktionstest mit jsdom (`npm install jsdom` in /tmp): `index.html` laden.
   Wichtig: `fetch` über die `beforeParse(window){…}`-Option setzen (nicht
   nachträglich), weil `load()` sofort beim Parsen feuert; `fetch` gibt die
   echte `newsletter_latest.json` zurück. Dann prüfen: Datum-Badge,
   Filter-Chips (inkl. Glas-Klassen), Anzahl Story-Karten pro Section, Klick
   auf einen Quellen-Chip filtert korrekt, und der Hell/Dunkel-Umschalter
   ändert `data-theme`, die `theme-color`-Meta und `localStorage('nr-theme')`.
   `localStorage` stellt jsdom selbst bereit — nicht überschreiben.
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
