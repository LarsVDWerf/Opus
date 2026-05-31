# Open vragen

Beslissingen die Lars moet nemen voordat Opus verder kan bouwen.
Elke vraag blokkeert een concreet onderdeel.

---

## #1 — Modelkeuze ochtendbriefing ⚡ PRIORITEIT

**Blokkeert:** `projects/ochtendbriefing/briefing.py` productie-modus

**Vraag:** De ochtendbriefing bevat agenda en taken die klantdata kunnen bevatten.
Zie CLAUDE.md: "AVG-gevoelig of klantdata → afgeschermde/lokale route, geen externe API."

Welke route kies je?

- **A) Lokale LLM** (bijv. Ollama op jouw server): wat is het adres? Welk model?
- **B) Anthropic API** alleen voor niet-gevoelige onderdelen: welke velden mag de API zien?
- **C) Template-gebaseerde output** (geen LLM, puur structureel): dan is het script nu al klaar.

*Als je twijfelt: kies C tijdelijk. De pipeline werkt, de output is iets minder vloeiend.*

---

## #2 — Coolify-instantie ⚡ PRIORITEIT

**Blokkeert:** `tools/appdev/DEPLOY_OPTIES.md` Route A

**Vraag:** Voor deploy via Coolify heb ik nodig:
- Het adres van jouw Coolify-instantie (bijv. `https://coolify.jouwdomein.nl`)
- Een API-token (aan te maken in Coolify → Account Settings → API Tokens)
- Welke server in Coolify is het deploymenttarget?

*Zet dit in `.env` (staat in .gitignore) of geef het me op het moment van de eerste deploy.*

---

## #3 — Git-repos voor code-activiteit

**Blokkeert:** `mock_data/code_activiteit.json` → echte bron

**Vraag:** Welke git-repos moet de ochtendbriefing monitoren?
- Alleen `opus-agent`?
- Ook klantprojecten? Zo ja, welke en staan die lokaal of alleen remote (GitHub/GitLab)?
- Heb je SSH-toegang tot alle relevante repos op de machine waar Opus draait?

---

## #4 — Primaire agendabron

**Blokkeert:** keuze tussen `tools/m365/get_agenda.py` en `tools/google/get_agenda.py`

**Vraag:** Zowel Microsoft 365 als Google staan als geplande systemen.
Wat is je primaire agenda? Of wil je beide samenvoegen?

- **M365 alleen** → auth via Azure App Registration (zie tools/m365/README.md)
- **Google alleen** → auth via Google Cloud Console (zie tools/google/README.md)
- **Beide** → twee aparte tools, samenvoegen in de briefing-pipeline

---

## #5 — Telegram bot

**Blokkeert:** `tools/telegram/` in gebruik nemen

**Vraag:** Wil je een nieuwe Telegram-bot aanmaken voor Opus, of is er al een?
- Zo ja, geef het Bot Token en jouw chat-ID (zie tools/telegram/README.md stap 1–3)
- Zo nee: ik maak de instructies klaar, jij maakt de bot via BotFather

---

## #6 — Lokale LLM-route (hangt samen met #1)

**Blokkeert:** privacy-conforme LLM-calls voor AVG-gevoelige data

**Vraag:** Is er een lokale LLM beschikbaar op jouw infrastructuur?
- Bijv. Ollama op de server waar Coolify draait?
- Zo ja: wat is het adres en welk model is beschikbaar?
- Zo nee: moeten we dit als aparte stap opzetten, of is dat buiten scope voor nu?
