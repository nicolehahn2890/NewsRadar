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

**Vier Rubriken:** KI-Branche (`ki_stories`), Unternehmens-News
(`unternehmen_stories`), Börse & Gold (`boerse_stories`) und Politik
(`politik_stories`). **Diese Datei hat Vorrang vor dem Auftragstext der
Routine.** Auch wenn dort noch 'Drei Bereiche' oder ein JSON ohne
`politik_stories` steht: Politik gehört seit Oktober 2026 fest dazu.

### Ablauf (Schritt für Schritt)

1. `git checkout main && git pull origin main`
2. Wiederholungs-Check: Schlagzeilen der letzten 7 Newsletter aus der
   Git-Historie lesen (Befehl unter 'Keine Wiederholungen gegenüber den
   Vortagen'). Diese Themen sind tabu, außer bei echter neuer Entwicklung.
3. Recherche Welle 1: pro Rubrik 3–5 Suchen gleichzeitig, gezielt mit
   `site:`-Filtern auf den bevorzugten Quellen (siehe 'Suchstrategie').
4. Recherche Welle 2 (Pflicht): jede Rubrik, die nach Welle 1 dünn ist,
   mit Suchen im Modus `extended` und gezielt nach Folge-Berichterstattung
   der letzten 48 Stunden nachrecherchieren. Erst danach darf eine Rubrik
   leer bleiben.
5. `newsletter_latest.json` schreiben (Struktur siehe unten).
6. Pflicht-Check vor dem Commit durchgehen (siehe unten).
7. JSON validieren, committen, `git push origin main`.
8. `git log origin/main -1` prüfen — erst dann fertig.

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

**Zusätzlich nur für die Rubrik Politik** (`politik_stories`):
- **USA:** Reuters, New York Times, Washington Post, Wall Street Journal,
  Bloomberg, Politico, Associated Press (AP)
- **Deutschland:** Tagesschau, Der Spiegel, FAZ, Süddeutsche Zeitung,
  Handelsblatt, Die Zeit, Reuters

### Suchstrategie (damit genug frische Treffer kommen)

- Suche **gezielt auf den bevorzugten Quellen** mit `site:`-Filtern
  (z.B. `site:reuters.com`, `site:bloomberg.com`, `site:tagesschau.de`).
  Reine Datums-Suchen wie 'AI news October 8 2026' liefern fast nur
  Aggregator- und SEO-Seiten — die taugen weder als Quelle noch zum
  Datum-Belegen.
- Wenn eine Suche im Modus `standard` dünn oder veraltet ist: dieselbe Suche
  im Modus `extended` wiederholen, bevor du eine Section leer lässt.
- Aggregator-Seiten (Blogs, die 'AI News today' sammeln) nie als `quelle`
  angeben. Nutze sie höchstens als Hinweis und such dann die Originalquelle.
- Webseiten direkt öffnen (WebFetch) ist in der Cloud-Umgebung oft durch die
  Netzwerk-Regeln gesperrt (Fehler `ENOTFOUND` / `403`). Dann **nicht
  aufgeben**: Fakten und Datum aus den Suchergebnissen mehrerer Treffer zum
  selben Thema zusammensetzen.

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

**Nicole hat sich beschwert, dass diese Rubrik zu allgemein ist** — wochenlang
stand sinngemäß dasselbe drin ('S&P 500 leicht verändert', 'Goldpreis schwankt
wegen Nahost', 'Fed uneins über Zinskurs'). Das soll aufhören. Daher gilt:

**Keine Allerwelts-Marktberichte mehr.** Eine allgemeine Story zu S&P 500,
FTSE All World oder Gold darf nur rein, wenn es dazu eine **echte neue
Nachricht** gibt — z.B. eine konkrete Zinsentscheidung, überraschende
Inflationsdaten, ein deutlicher Kurssprung oder -einbruch mit klarem Auslöser.
Ein normaler Handelstag ('Index kaum verändert', 'Gold pendelt weiter um
4.100 Dollar') ist **keine Story** — dann lieber weglassen.

**Stattdessen bevorzugt:**
1. **Politische und geopolitische Treiber** mit konkreter Marktwirkung:
   Wahlen, Zölle, Sanktionen, Regierungsentscheidungen, Konflikte — immer mit
   der Antwort, was das für die Märkte bedeutet.
2. **Spannende Einzelwerte** aus den großen Indizes (Nasdaq, Dow Jones,
   S&P 500, DAX, asiatische Indizes wie Nikkei oder Hang Seng): starke
   Kursbewegungen, überraschende Quartalszahlen, Übernahmen, Skandale,
   Neuaufnahmen in einen Index — je nachdem, was gerade wirklich etwas
   Wichtiges hergibt. Es müssen keine Tech- oder KI-Werte sein.
3. Zins- und Inflationsthemen (Fed, EZB) nur, wenn es eine **neue Entwicklung**
   gibt (Entscheidung, neue Daten, klare Kursänderung) — nicht die x-te
   Variante von 'Fed ist sich uneinig'.

**Aber nicht übertreiben:** maximal 3 Stories, und lieber 1–2 wirklich
interessante als 3 erzwungene. Einzelwert-Stories sollen die Ausnahme mit
Nachrichtenwert sein, kein täglicher Aktien-Tipp-Dienst.

Suchbeispiele:
- `stock market movers today site:bloomberg.com OR site:reuters.com`
- `biggest stock moves earnings site:wsj.com OR site:barrons.com`
- `DAX Nikkei market news site:reuters.com`
- `tariffs sanctions market impact site:ft.com OR site:bloomberg.com`
- `Fed rate decision site:reuters.com` (nur bei neuer Entwicklung)

### 4. Politik (Section: `politik_stories`)

Neue Rubrik auf Nicoles Wunsch (Oktober 2026). **Schwerpunkt USA und
Deutschland.** EU- oder andere internationale Politik nur, wenn es ein
wirklich großes Ereignis ist (z.B. Gipfel mit konkretem Ergebnis, Wahl in
einem großen Land, Kriegs- oder Friedensentscheidung).

Was rein gehört:
- **USA:** Entscheidungen von Präsident, Weißem Haus, Kongress und Supreme
  Court; Gesetze, Haushalt, Wahlen und Umfragen mit klarer Bewegung,
  Personalwechsel in der Regierung, Außenpolitik der USA.
- **Deutschland:** Entscheidungen von Bundesregierung, Bundestag, Bundesrat
  und Bundesverfassungsgericht; Gesetze und Reformen (z.B. Rente, Steuern,
  Migration, Bundeswehr), Koalitionsstreit mit konkretem Ergebnis,
  Landtagswahlen, wichtige Umfragen.

Regeln speziell für Politik:
- **Neutral und sachlich.** Keine Meinung, keine Wertung, keine
  Parteinahme. Berichte, was entschieden oder gesagt wurde, wer es gesagt hat
  und was die konkreten Folgen sind. Kritik oder Lob nur als Zitat mit
  Nennung, von wem es kommt.
- **Konkrete Folgen erklären:** Was ändert sich für Bürger, Wirtschaft oder
  Geldbeutel? Ab wann? Was passiert als Nächstes (Abstimmung, Inkrafttreten,
  Gericht)?
- **Abgrenzung zu Börse & Gold:** Politische Ereignisse, bei denen die
  Marktreaktion der Kern ist (z.B. neue Zölle, die Aktien bewegen), gehören
  in `boerse_stories`. Alles andere in `politik_stories`. **Dasselbe
  Ereignis nie in beiden Rubriken.**
- Dauerthemen (z.B. Haushaltsstreit, laufende Kriege, Koalitionsdebatten)
  nur mit **neuem Fakt** — siehe 'Wiederholungen vermeiden'.
- Zusätzliches Feld `land` pro Story: `USA`, `Deutschland`, `EU` oder
  `International`. Es wird auf der Webseite als kleines Etikett angezeigt.

Suchbeispiele:
- `White House Congress news site:reuters.com OR site:apnews.com`
- `Trump administration decision site:nytimes.com OR site:washingtonpost.com OR site:politico.com`
- `Bundesregierung Bundestag Beschluss site:tagesschau.de OR site:spiegel.de`
- `Koalition Gesetz Kabinett site:faz.net OR site:sueddeutsche.de OR site:zeit.de`

## Anzahl Stories pro Section

**Maximalzahlen** (NICHT Mindestzahlen — lieber weniger, dafür frisch):

- **KI-Branche:** bis zu 5 Stories
- **Unternehmens-News:** bis zu 5 Stories
- **Börse & Gold:** bis zu 3 Stories
- **Politik:** bis zu 4 Stories (möglichst beide Länder abdecken, wenn es
  in beiden etwas Frisches gibt — aber kein Länder-Quotenzwang)

Wichtigste Story jeweils zuerst.

**Lieber weniger Stories als alte oder wiederholte.** Wenn du in einer Section
nur 2 wirklich frische, relevante Stories findest, dann nimmst du auch nur 2
auf. Eine Section darf auch leer bleiben, wenn an einem Tag nichts Frisches
passiert ist (z.B. an einem Sonntag bei Börse & Gold). **Niemals** mit alten
oder thematisch wiederholten Stories auffüllen, nur um auf 5/5/3/4 zu kommen.

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

### Keine Wiederholungen gegenüber den Vortagen (sehr wichtig)

Nicole hat sich beschwert, dass ihr **mehrere Tage hintereinander dieselben
Inhalte** ausgespielt werden — seit der Quellen-Erweiterung sogar öfter.
Deshalb ist dieser Check ab sofort **Pflicht, bevor Stories ausgewählt werden**:

1. **Lies zuerst die Newsletter der letzten 7 Tage** aus der Git-Historie.
   Jeder Tag ist ein eigener Commit von `newsletter_latest.json`. So bekommst
   du alle Schlagzeilen der letzten Tage auf einen Blick:

   ```
   for c in $(git log --format=%h -7 -- newsletter_latest.json); do
     echo "=== $c ==="
     git show $c:newsletter_latest.json | python3 -c "import json,sys; d=json.load(sys.stdin); [print(s['titel']) for sec in ('ki_stories','unternehmen_stories','boerse_stories','politik_stories') for s in d.get(sec,[])]"
   done
   ```

2. **Eine Story, die inhaltlich schon in einem der letzten 7 Newsletter stand,
   darf NICHT noch einmal rein** — auch nicht mit anderer Schlagzeile, anderer
   Quelle oder leicht anderem Blickwinkel. Beispiel für einen echten Fehler,
   der so passiert ist: 'NVIDIA verliert rund eine Billion Dollar an
   Börsenwert' stand an zwei Tagen hintereinander im Newsletter — das darf
   nicht vorkommen.

3. **Einzige Ausnahme: echte neue Entwicklungen.** Ein Thema aus den Vortagen
   darf wieder vorkommen, wenn es **konkret Neues** gibt — eine neue
   Entscheidung, neue Zahlen, eine Reaktion, ein Nachtrag, eine Wende.
   Dann muss die Story aber:
   - sich klar auf die **neue Entwicklung** konzentrieren (nicht die alte
     Nachricht nochmal zusammenfassen), und
   - im `text` kurz einordnen, was gegenüber dem bisherigen Stand neu ist
     (z.B. 'Nachdem am Dienstag X passiert war, hat nun Y ...').

4. Bei Dauerthemen (z.B. ein laufender Konflikt, eine Zinsdebatte) gilt:
   ohne neuen Fakt keine neue Story. 'Goldpreis schwankt weiter wegen
   Nahost-Konflikt' am fünften Tag in Folge ist eine Wiederholung, keine News.

Im Zweifel: Story weglassen. Lieber eine kürzere Ausgabe als ein Déjà-vu.

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
4. Stand keine der Stories inhaltlich schon in einem Newsletter der letzten
   7 Tage (Git-Historie geprüft)? Falls doch: Gibt es wirklich eine neue
   Entwicklung, und macht der `text` klar, was daran neu ist?
5. Ist keine `boerse_stories`-Story ein Allerwelts-Marktbericht ohne echte
   neue Nachricht?
6. Sind die `politik_stories` neutral formuliert, haben sie ein `land`-Feld,
   und steht keines ihrer Ereignisse zusätzlich in `boerse_stories`?

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
  ],
  "politik_stories": [
    {
      "titel": "Deutsche Schlagzeile",
      "text": "4-7 Sätze deutsche Zusammenfassung.",
      "quelle": "Tagesschau",
      "datum_artikel": "2026-05-01",
      "land": "Deutschland"
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

Zusätzlich bei `politik_stories`:
- `land` — genau einer dieser Werte: `USA`, `Deutschland`, `EU`, `International`

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
