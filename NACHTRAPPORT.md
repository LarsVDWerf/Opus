# Nachtrapport — 2026-05-31

## De twee beslissingen die je vandaag moet nemen

**1. Modelkeuze ochtendbriefing (OPEN_VRAGEN.md #1)**
De pipeline draait, maar de LLM-call staat op mock. Agenda en taken kunnen klantdata bevatten — CLAUDE.md vereist een lokale route of bewuste keuze. Kies: lokale LLM / Anthropic API voor niet-gevoelig deel / template-output. Zonder deze keuze blijft de briefing gesimuleerd.

**2. Coolify-adres en server (OPEN_VRAGEN.md #2)**
Zonder dit kan ik de app-dev capability niet praktisch testen. Zodra ik het adres en een API-token heb, kan ik Route A in DEPLOY_OPTIES.md concreet uitwerken en een eerste echte scaffold deployen.

---

## Wat is gebouwd

### tools/ — capability-steiger
- `tools/m365/README.md` — auth-stappen Azure, geplande scripts voor agenda/mail/Teams
- `tools/google/README.md` — auth-stappen Google Cloud, geplande scripts voor Gmail/Calendar
- `tools/clickup/README.md` — auth via Personal API Token, geplande scripts voor taken en activiteit
- `tools/jortt/README.md` — auth via Jortt API, read-only facturen en overzicht
- `tools/telegram/README.md` — auth via BotFather, berichten ontvangen en concept-sturen

Elke README beschrijft: wat de tool doet, welke API en credentials nodig zijn, concrete aanmaakstappen, en geplande script-interfaces (inputs/outputs).

### projects/ochtendbriefing/ — werkende pipeline
- `briefing.py` — draaibaar script: data ophalen → samenvoegen → LLM-call → alinea
- `mock_data/*.json` — vier gemarkeerde mock-bestanden (agenda, taken, code, collega's)
- `prompt.md` — LLM-prompt template voor de echte call

**Draai nu:** `python3 projects/ochtendbriefing/briefing.py`
Produceert een voorbeeld-briefing op nepdata. Elke TODO markeerst waar een echte bron inkomt.

### tools/appdev/ — app-dev draaiboek
- `DRAAIBOEK.md` — 7 fases, 8 expliciete STOP-punten waar jouw input of goedkeuring vereist is
- `DEPLOY_OPTIES.md` — drie deploy-routes (Coolify, Docker, alternatief) met benodigdheden en risico's
- `MONITORING.md` — wat Opus monitort, rapportageformat, grenzen aan autonoom verbeteren
- `voorbeeld/` — minimale FastAPI-scaffold (syntaxis gevalideerd, lokaal te draaien)

### memory/ — startstructuur
Lege bestanden met kopjes: `klanten.md`, `projecten.md`, `voorkeuren.md`, `werkritme.md`, `besluiten.md`.

---

## Wat werkt (op mockdata)
- Ochtendbriefing-pipeline draait en produceert output
- Voorbeeld-app is syntactisch correct en lokaal te starten

## Wat bewust NIET is gedaan
- Geen enkele echte API-call, token of credential
- Geen deploy van wat dan ook
- Geen verbindingen naar externe systemen
- CLAUDE.md niet aangeraakt
- Niets buiten /home/opus/opus-agent/ geraakt

## Openstaande vragen (samenvatting)
Zie OPEN_VRAGEN.md voor volledig detail.

| # | Vraag | Blokkeert |
|---|---|---|
| 1 | Modelkeuze ochtendbriefing (AVG-afweging) | Productie-briefing |
| 2 | Coolify-adres en API-token | App deploy Route A |
| 3 | Welke git-repos monitoren? | Code-activiteit in briefing |
| 4 | Primaire agendabron (M365 of Google?) | Welke tool eerst te bouwen |
| 5 | Telegram bot (nieuw of bestaand?) | Telegram-integratie |
| 6 | Lokale LLM beschikbaar? | AVG-conforme LLM-calls |

---

*Gebouwd door Opus in één autonome sessie. Alle grenzen uit de opdracht zijn gerespecteerd.*
