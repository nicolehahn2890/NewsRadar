# NewsRadar – Daily News Agent

## Verhaltensregeln für den Agenten
- Behaupte nichts was du nicht weißt oder überprüft hast
- Bei Unsicherheit: klar sagen "ich bin nicht sicher" statt etwas erfinden
- Fakten wie Termine, Kurse, News immer aus echten Quellen belegen

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

- **KI-Branche:** 5 Stories
- **Unternehmens-News:** 5 Stories
- **Börse & Gold:** 3 Stories

Wichtigste Story jeweils zuerst.

## Output: `newsletter_latest.json`

Schreibe das Ergebnis in `newsletter_latest.json` im Repository-Root, dann
commit und push auf den `main` Branch.

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

## Commit

- Commit-Message: `Newsletter [Datum]` (z.B. `Newsletter 2026-05-02`)
- Push auf `main`

## Important Notes

- Verwende immer das **heutige tatsächliche Datum** in den Suchanfragen
- Wenn eine Quelle zu einem Thema nichts hat, nimm die nächstbeste
- Keine erfundenen Fakten, keine erfundenen URLs
- Wenn du dir bei einer Übersetzung unsicher bist: behalte den englischen
  Begriff in Klammern dahinter
