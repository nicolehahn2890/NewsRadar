# NewsRadar – Daily Newsletter Agent

## Verhaltensregeln für den Agenten
- Behaupte nichts was du nicht weißt oder überprüft hast
- Bei Unsicherheit: klar sagen "ich bin nicht sicher" statt etwas erfinden
- Fakten wie Termine, Kurse, News immer aus echten Quellen belegen

This file defines the instructions for the automated daily newsletter agent.

## Schedule

Runs **3x per week**: Monday, Wednesday, Saturday at **05:00 Uhr (Europe/Vienna)**.

## Task

Research and send a comprehensive daily briefing email to **nicole.hahn2890@gmail.com**.

## Token Efficiency

To save tokens, use the pre-built template in `newsletter_template.html`. Read that file and replace only the `{{PLACEHOLDERS}}` with fresh content. Do NOT regenerate the full HTML from scratch.

Key placeholders:
- `{{DATUM}}` — heutiges Datum auf Deutsch
- `{{DAX_WERT}}`, `{{DAX_PCT}}`, `{{DAX_COLOR}}` — Kurswert, %-Änderung, Farbe (#4ab880 grün / #e06060 rot)
- Same pattern for `SP` and `GOLD`
- `{{KI1_TAG}}` bis `{{KI5_TAG}}` — z.B. `🟣 CLAUDE — NEUES FEATURE`
- `{{KI1_TITEL}}` bis `{{KI5_TITEL}}` — Schlagzeile
- `{{KI1_TEXT}}` bis `{{KI5_TEXT}}` — 2–3 Sätze Zusammenfassung
- `{{KI1_QUELLE}}` bis `{{KI5_QUELLE}}` — Quellenangabe
- `{{MARKT_BOX_BG}}` / `{{MARKT_BOX_BORDER}}` — `#fff8e6` / `#fbbf24` (Warnung) oder `#f0fdf4` / `#4ab880` (positiv)
- `{{MARKT_BOX_LABEL_COLOR}}` — `#b45309` (Warnung) oder `#166534` (positiv)
- `{{MARKT_BOX_LABEL}}` — z.B. `⚠ MÄRKTE UNTER DRUCK`
- `{{MARKT_KOMMENTAR}}` — aktueller Marktkommentar
- `{{ANLAGEN_TEXT}}` — Einschätzung für FTSE All World, Small Caps, Gold
- `{{WELT1_TAG}}` / `{{WELT1_TITEL}}` / `{{WELT1_TEXT}}` — Weltwirtschaft Story 1
- `{{WELT2_TAG}}` / `{{WELT2_TITEL}}` / `{{WELT2_TEXT}}` — Weltwirtschaft Story 2

## Research Topics

### 1. KI & Modelle (most important)
Search for the latest news on:
- **Anthropic / Claude**: new models, features, Claude Code updates, API changes, research papers
- **OpenAI / ChatGPT**: GPT model releases, new features, company news
- **Google / Gemini**: Gemini model updates, Google AI products, integrations
- **Perplexity AI**: product updates, new features
- **KI Allgemein**: AI industry news, new tools, breakthroughs, regulation, use cases

Use these search queries (adapt date to today):
- `"Claude Anthropic" neue Features aktuell 2026`
- `"OpenAI ChatGPT" aktuell Neuigkeiten 2026`
- `"Google Gemini" aktuell Update 2026`
- `Perplexity AI news 2026`
- `KI künstliche Intelligenz Nachrichten aktuell`

### 2. Märkte & ETFs
Search for:
- DAX aktuell Kurs heute
- S&P 500 aktuell heute
- Gold Preis aktuell heute
- FTSE All World ETF news aktuell
- Small Caps ETF Entwicklung aktuell
- Bitcoin aktuell

### 3. Weltwirtschaft
Search for:
- Weltwirtschaft aktuell heute
- Inflation Zinsen Zentralbank aktuell
- KI Aktien Tech Börse aktuell

## Email Format

Send an HTML email with this structure:

### Header (dark, #0a0f1a background)
- "▓▓ NEWSRADAR ▓▓" in monospace green (#4ab880)
- "NewsRadar" title, "Radar" in rose (#c98878)
- Today's date in German (e.g. "Mittwoch, 1. April 2026")
- Live ticker bar: DAX · S&P500 · GOLD with current values and % change (green ▲ / red ▼)

### Section 1: KI & MODELLE (purple accent #a78bfa)
- 4–6 stories, most important first
- Each story: source tag (🟣 CLAUDE · ⚪ OPENAI · 🔵 GEMINI · 🟡 PERPLEXITY · 🤖 KI ALLGEMEIN)
- Large bold headline (18–22px Georgia serif)
- 2–3 sentence summary in plain language
- Source name at bottom in monospace

### Section 2: MÄRKTE & ETFs (green accent #4ab880)
- Dark boxes showing DAX, S&P 500, Gold with price and % change
- Yellow highlight box for negative market news
- Green highlight box for Nicole's specific holdings:
  - FTSE All World ETF
  - Small Caps ETF  
  - Gold
- Always include a brief assessment: what does today's market mean for these holdings?

### Section 3: WELTWIRTSCHAFT (orange accent #fb923c)
- 1–2 most relevant macro stories
- Focus on what affects tech stocks, AI sector, and ETF performance

### Footer (dark)
- "▓ NEWSRADAR ▓" · daily 05:00 Uhr · Keine Anlageberatung

## Style Rules
- Mix NYT editorial (Georgia serif headings, clean layout) with arcade/terminal (Courier New monospace for labels, dark boxes, pixel-style section headers)
- Background: white/cream (#fff) for article area, dark (#0a0f1a) for header/footer
- Be thorough — Nicole wants to miss nothing
- Write in German throughout
- All inline CSS (email client compatibility)
- Max width: 600px

## Send via Gmail
1. Use `gmail_create_draft` to create the email with full HTML content
2. Then use `gmail_send_draft` with the returned draftId to actually **send** it — do NOT leave it as a draft
3. Recipient: nicole.hahn2890@gmail.com
4. Subject format: `📡 NewsRadar · [Weekday], [Day]. [Month] [Year]`
   Example: `📡 NewsRadar · Mittwoch, 1. April 2026`

## Important Notes
- Always use today's actual date in search queries and the email subject
- Be thorough — research at least 5–7 AI stories and all key market data
- The email must be **sent**, not just saved as draft
- Write everything in German
- Never skip sections — Nicole wants a complete daily overview
