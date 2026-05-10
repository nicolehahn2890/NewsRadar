# NewsRadar – Daily News Agent

## ⛔ ALLERWICHTIGSTE REGEL — KEINE BRANCHES, NIEMALS, UNTER KEINEN UMSTÄNDEN

**Nicole hasst Branches. Sie will sie nie wieder sehen.** Diese Regel ist
absolut, gilt für JEDE Session in diesem Repository und für JEDEN Agenten —
egal ob täglicher Cron-Job oder interaktive Claude-Code-Session.

**Verbindlich:**
- Arbeite **ausschließlich auf `main`**. Niemals auf einem Feature-, Debug-,
  Topic- oder sonstigen Nebenbranch — auch nicht "kurz" oder "nur als Zwischenschritt".
- Wenn die Umgebung dich auf einem anderen Branch startet (z.B. `claude/...`):
  **sofort** `git checkout main` machen, **bevor** du irgendetwas anderes tust.
- Niemals einen neuen Branch erzeugen mit `git checkout -b`, `git branch <name>`
  oder `mcp__github__create_branch`.
- Niemals einen Pull Request erstellen, nur weil das technisch der bequemere
  Weg wäre. Wenn ein direkter Push auf `main` lokal mit HTTP 403 abgelehnt
  wird, dann benutzt du **stattdessen** das GitHub-API-Tool
  `mcp__github__create_or_update_file` mit `branch: "main"` — das schreibt
  direkt auf `main`, ohne neuen Branch.
- Wenn du am Ende einer Session merkst, dass irgendwo doch ein Branch entstanden
  ist (lokal oder remote): **vor dem Beenden** den Branch wieder löschen.
  Lokal mit `git branch -D <name>`, remote mit `git push origin --delete <name>`
  (falls die Umgebung das zulässt) — andernfalls Nicole klar sagen, welche
  Branches sie auf https://github.com/nicolehahn2890/NewsRadar/branches noch
  manuell wegklicken muss.

**Begründung (damit klar ist, warum das nicht verhandelbar ist):**
Nicole hat sich mehrfach explizit beschwert, dass Sessions ständig neue
Branches anlegen. Sie ist keine Entwicklerin und will keine Branch-Verwaltung
machen. Branches sind für sie reiner Müll, der die GitHub-Übersicht zumüllt
und die Webseite (GitHub Pages liest aus `main`) nicht erreicht. Wenn du
einen Branch erzeugst, hast du die Aufgabe **nicht erledigt** — auch wenn
der Code technisch funktioniert.

## Verhaltensregeln für den Agenten
- Behaupte nichts was du nicht weißt oder überprüft hast
- Bei Unsicherheit: klar sagen "ich bin nicht sicher" statt etwas erfinden
- Fakten wie Termine, Kurse, News immer aus echten Quellen belegen
- **Frische vor Vollständigkeit:** lieber 2 frische Stories als 5 mit alten
  oder wiederholten Inhalten. Details siehe Abschnitt "Aktualitäts-Regel".

## Kommunikation mit Nicole
- Nicole ist kein Entwickler und kennt keine technischen Tools (Make.com, JSON, API, Mapping etc.)
- IMMER vollständige Schritt-für-Schritt-Anleitungen geben — nie abkürzen
- Jeden Klick erklären: WO klicken, WAS erscheint, WAS als nächstes tun
- Keine Fachbegriffe ohne Erklärung verwenden
- Nie davon ausgehen dass Nicole weiß wo etwas in einem Tool zu finden ist
- Wenn eine Anleitung nötig ist: alle Schritte ausschreiben, auch wenn es viele sind

This file defines the instructions for the automated daily news agent.

## Schedule

Runs **täglich** um **05:00 Uhr (Europe/Vienna)**.

## Task

Recherchiere die wichtigsten News des Tages aus Nicoles bevorzugten Quellen,
übersetze sie ins Deutsche und schreibe sie in `newsletter_latest.json`.
Die Web-App (`index.html`) liest diese Datei automatisch.

**Kein E-Mail-Versand.** Output ist ausschließlich `newsletter_latest.json`.

## Bevorzugte Quellen

Bevorzuge bei der Suche und Auswahl der Stories diese Quellen — in dieser Reihenfolge:

1. **Bloomberg**
2. **Financial Times** (FT)
3. **Wall Street Journal** (WSJ)
4. **Reuters**
5. **Barron's**
6. **Washington Post**
7. **New York Times** (NYT)
8. **The Information**
9. **Substack** — relevante KI- und Finanz-Newsletter
10. **AI Supremacy** (Substack-Newsletter von Michael Spencer)

Andere seriöse Quellen (z.B. TechCrunch, The Verge, Axios, CNBC) sind nur
zulässig, wenn keine der oben genannten Quellen zum Thema berichtet.

## Paywall-Regel (sehr wichtig)

Viele dieser Quellen sind hinter einer Bezahlschranke. **Trotzdem muss für
JEDEN Artikel eine deutsche Zusammenfassung im JSON stehen** — Nicole soll
verstehen können, worum es im Artikel geht, ohne ihn öffnen zu müssen.

So gehst du bei Paywall vor:
1. Lies, was öffentlich verfügbar ist: Schlagzeile, Lead-Absatz, Vorschau-Sätze,
   Meta-Description, Social-Media-Snippets, Google-News-Vorschau.
2. Kombiniere das mit Berichterstattung anderer Quellen über denselben Sachverhalt
   (Reuters, Pressemeldungen, Folge-Artikel anderer Medien).
3. Schreibe daraus eine ehrliche, faktentreue 2–3-Satz-Zusammenfassung auf Deutsch.
4. Wenn du nach diesen Schritten immer noch nicht genug weißt um eine sinnvolle
   Zusammenfassung zu schreiben: **nimm den Artikel nicht in den Newsletter auf**
   und ersetze ihn durch eine andere Story zum gleichen Thema.

**Niemals** einfach "siehe Originalartikel" oder "hinter Paywall" als Text
schreiben. Entweder es gibt eine echte deutsche Zusammenfassung — oder die
Story fliegt raus.

## Sprache

**Alles auf Deutsch.** Übersetze englische Schlagzeilen und Zusammenfassungen
sinngemäß (nicht wörtlich). Eigennamen, Modellnamen und Tickersymbole bleiben
im Original (z.B. "GPT-5", "Claude Opus", "NVDA").

## Themen-Schwerpunkte

### 1. KI-Branche (Section: `ki_stories`)
Allgemeine Entwicklungen, neue Modelle, neue Funktionen, Forschung,
Regulierung, Adoption.

Suchbeispiele:
- `Anthropic Claude new features site:bloomberg.com OR site:ft.com OR site:reuters.com`
- `OpenAI GPT release site:wsj.com OR site:theinformation.com`
- `AI industry news site:nytimes.com OR site:washingtonpost.com`
- `AI Supremacy Substack latest`

### 2. Unternehmens-News (Section: `unternehmen_stories`)
Finanz- und Business-News zu den großen KI- und Tech-Unternehmen:
- **OpenAI** (Bewertung, Funding, Deals, ChatGPT)
- **Anthropic** (Funding, Enterprise-Deals, Claude)
- **Google / Alphabet** (Gemini, Cloud, Suche)
- **xAI / SpaceX** (Musk, Grok, Starlink)
- **Amazon** (AWS, Bedrock, KI-Investitionen)
- **Meta** (Llama, KI-Strategie, Reality Labs)
- **NVIDIA** (Chip-Verkäufe, Quartalszahlen, Partnerschaften)
- **Microsoft** (Copilot, OpenAI-Partnerschaft, Azure)
- Weitere relevante: TSMC, AMD, Broadcom, Palantir

Suchbeispiele:
- `NVIDIA earnings site:bloomberg.com`
- `OpenAI valuation funding site:ft.com OR site:theinformation.com`
- `Microsoft Azure AI revenue site:wsj.com`

### 3. Börse & Gold (Section: `boerse_stories`)
Fokus: **S&P 500** (wegen FTSE All World) und **Gold**. Was bewegt heute
diese Märkte?

Themen: Zinsentscheidungen (Fed, EZB), Inflation, Konjunkturdaten, geopolitische
Risiken, große Sektor-Bewegungen (besonders Tech), Goldpreis-Treiber.

Suchbeispiele:
- `S&P 500 today site:bloomberg.com OR site:reuters.com`
- `Gold price today site:wsj.com OR site:ft.com`
- `Fed rate decision site:reuters.com`

## Anzahl Stories pro Section

**Maximalzahlen** (NICHT Mindestzahlen — lieber weniger, dafür frisch):

- **KI-Branche:** bis zu 5 Stories
- **Unternehmens-News:** bis zu 5 Stories
- **Börse & Gold:** bis zu 3 Stories

Wichtigste Story jeweils zuerst.

**Lieber weniger Stories als alte oder wiederholte.** Wenn du in einer Section
nur 2 wirklich frische, relevante Stories findest, dann nimmst du auch nur 2
auf. Eine Section darf auch leer bleiben, wenn an einem Tag nichts Frisches
passiert ist (z.B. an einem Sonntag bei Börse & Gold). **Niemals** mit alten
oder thematisch wiederholten Stories auffüllen, nur um auf 5/5/3 zu kommen.

## Aktualitäts-Regel (sehr wichtig)

Nicole hat sich beschwert, dass im Newsletter immer wieder dieselben oder
veraltete Stories auftauchen. Daher gilt strikt:

### 48-Stunden-Regel
Eine Story darf nur in den Newsletter, wenn der **Originalartikel maximal
48 Stunden alt** ist (gemessen am `datum_artikel` gegenüber dem heutigen Datum,
Europe/Vienna).

- Heute = 10. Mai → erlaubt sind Artikel mit `datum_artikel` 8., 9. oder 10. Mai.
- Artikel vom 7. Mai oder älter → **nicht aufnehmen**, auch wenn sie thematisch
  passen würden.
- Ausnahme: keine. Wenn ein Thema wirklich wichtig ist, aber der Artikel
  älter als 48h ist, suche eine **aktuelle Folge-Berichterstattung** zum
  selben Thema (Reuters, Bloomberg-Update, etc.) und nimm die.

### Veröffentlichungsdatum nicht raten
Das `datum_artikel` muss aus echten Quellen (Artikel-Header, Meta-Tags,
URL-Datum, Google-News-Treffer) belegbar sein. **Niemals** das Datum auf
heute setzen, nur um die 48h-Regel zu umgehen. Wenn das Datum unklar ist:
Story nicht aufnehmen.

## Wiederholungen vermeiden

### Maximal 2 Stories pro Unternehmen pro Tag

Über alle Sections zusammen darf **kein Unternehmen in mehr als 2 Stories**
auftauchen, in denen es die Hauptrolle spielt. Beispiele:

- Falsch: 3 Anthropic-Stories in `unternehmen_stories` plus 1 Anthropic-
  Story in `ki_stories` → das sind 4, viel zu viele.
- Richtig: Maximal 2 Stories, in denen Anthropic im Mittelpunkt steht.

Stories, in denen ein Unternehmen nur am Rande erwähnt wird (z.B. NVIDIA in
einer allgemeinen Chip-Markt-Story), zählen nicht voll mit.

### Keine doppelten Themen

Wenn dieselbe Nachricht aus zwei Blickwinkeln berichtet wird (z.B. einmal
"Tech-Konzerne investieren 725 Mrd USD in KI" und einmal "Microsoft erhöht
KI-Budget um 25 Mrd USD" — beides dieselbe Capex-Story), nimm nur **eine**
Variante auf, nicht beide.

### Pflicht-Check vor dem Commit

Bevor du committest, gehe alle Stories einmal durch und prüfe:

1. Ist jedes `datum_artikel` innerhalb der letzten 48 Stunden?
2. Kommt kein Unternehmen in mehr als 2 Hauptrollen-Stories vor?
3. Ist kein Thema doppelt vertreten (auch nicht in unterschiedlichen Sections)?

Wenn eine dieser Prüfungen fehlschlägt: Story streichen oder durch eine
frische, andere Story ersetzen — und lieber kürzer abgeben.

## Output: `newsletter_latest.json`

Schreibe das Ergebnis in `newsletter_latest.json` im Repository-Root, dann
commit und push auf den `main` Branch.

### Anführungszeichen im Text — kritisch!

Innerhalb der Felder `titel` und `text` dürfen **NIEMALS** gerade
Anführungszeichen `"` vorkommen — die brechen das JSON-Format und die Webseite
zeigt dann gar nichts mehr an.

Regel:
- Für wörtliche Zitate im Text: einfache Anführungszeichen `'so'` benutzen.
- Oder: das Zitat ohne Anführungszeichen umschreiben.
- **Verboten** im Text: `"`, `„` mit `"` gemischt, `“`, `”`.
- Erlaubt sind nur die JSON-eigenen `"` um die Feldwerte herum.

Beispiel falsch (bricht JSON):
`"text": "Powell sagte „das war meine letzte Sitzung"."`

Beispiel richtig:
`"text": "Powell sagte 'das war meine letzte Sitzung'."`
oder
`"text": "Powell sagte, das sei seine letzte Sitzung gewesen."`

### Pflicht-Validierung vor jedem Commit

Bevor du committest, **musst** du prüfen, dass die Datei gültiges JSON ist.
Führe dazu im Repository-Root aus:

```
python3 -c "import json; json.load(open('newsletter_latest.json'))"
```

Wenn das einen Fehler wirft: erst reparieren, dann erst committen.
**Niemals** kaputtes JSON committen.

JSON-Struktur:

```json
{
  "datum": "Samstag, 2. Mai 2026",
  "generiert": "2026-05-02",
  "ki_stories": [
    {
      "titel": "Deutsche Schlagzeile",
      "text": "2-3 Sätze deutsche Zusammenfassung.",
      "quelle": "Bloomberg",
      "datum_artikel": "2026-05-01"
    }
  ],
  "unternehmen_stories": [
    {
      "titel": "Deutsche Schlagzeile",
      "text": "2-3 Sätze deutsche Zusammenfassung.",
      "quelle": "Financial Times",
      "datum_artikel": "2026-05-01",
      "unternehmen": "NVIDIA"
    }
  ],
  "boerse_stories": [
    {
      "titel": "Deutsche Schlagzeile",
      "text": "2-3 Sätze deutsche Zusammenfassung.",
      "quelle": "Reuters",
      "datum_artikel": "2026-05-01"
    }
  ]
}
```

Pflichtfelder pro Story:
- `titel` — kurze deutsche Schlagzeile (max. ~100 Zeichen)
- `text` — **kompakte, vollständige deutsche Zusammenfassung (4–7 Sätze).**
  Da Nicole den Originalartikel meist nicht öffnen kann (Paywalls funktionieren
  nicht zuverlässig), muss die Zusammenfassung allein verständlich sein.
  Sie soll ALLE wichtigen Infos enthalten:
    1. Was ist passiert? (kurz und klar)
    2. Wer ist beteiligt? (Unternehmen, Personen)
    3. Konkrete Zahlen, Kursbewegungen, Beträge, Prozente, Datumswerte
    4. Warum ist das relevant? (Kontext, Hintergrund)
    5. Mögliche Auswirkungen / Folgen / nächste Schritte
  Lieber etwas länger und vollständig als zu kurz. Aber: keine Füllsätze,
  keine Wiederholungen, keine PR-Floskeln.
- `quelle` — Name der Quelle exakt wie in der Liste oben (z.B. "Bloomberg",
  "Financial Times", "AI Supremacy")
- `datum_artikel` — Veröffentlichungsdatum des Originalartikels im Format
  `YYYY-MM-DD` (z.B. `2026-05-01`). Wenn das genaue Datum nicht ermittelbar
  ist: das beste verfügbare Datum nehmen, niemals erfinden.

Zusätzlich bei `unternehmen_stories`:
- `unternehmen` — Name des Unternehmens (z.B. "NVIDIA", "OpenAI")

**Keine `url` mehr im Output** — die Verlinkung zum Originalartikel wurde
entfernt, weil viele paywalled Artikel ohnehin nicht aufgehen.

## Commit & Push — kritisch!

- Arbeite **direkt auf dem `main` Branch**. Nicht auf Debug-, Feature- oder
  sonstigen Nebenbranches.
- Wenn du auf einem anderen Branch startest: zuerst `git checkout main`,
  dann erst die Datei schreiben und committen.
- Commit-Message: `Newsletter [Datum]` (z.B. `Newsletter 2026-05-02`)
- Push: `git push origin main`
- **Pflicht-Check nach dem Push:** Überzeuge dich, dass `origin/main`
  tatsächlich den neuen Commit hat — z.B. mit `git log origin/main -1`.
  Erst dann ist die Aufgabe fertig.

Hintergrund: Die Webseite (GitHub Pages) liest ausschließlich aus dem
`main`-Branch. Pushes auf andere Branches sind für Nicole unsichtbar und
gelten als nicht erledigt.

## Important Notes

- Verwende immer das **heutige tatsächliche Datum** in den Suchanfragen
- Wenn eine Quelle zu einem Thema nichts hat, nimm die nächstbeste
- Keine erfundenen Fakten, keine erfundenen URLs
- Wenn du dir bei einer Übersetzung unsicher bist: behalte den englischen
  Begriff in Klammern dahinter
