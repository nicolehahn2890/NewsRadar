# NewsRadar – Daily Newsletter Agent

This file defines the instructions for the automated daily newsletter agent.

## Task

Every morning, research and send a comprehensive daily briefing email to **nicole.hahn2890@gmail.com**.

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
Use the gmail tools to create and send the draft to nicole.hahn2890@gmail.com.
Subject format: `📡 NewsRadar · [Weekday], [Day]. [Month] [Year]`
