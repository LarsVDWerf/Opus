# Tool: ClickUp

## Wat doet deze tool
Toegang tot ClickUp voor taakbeheer. Drie verantwoordelijkheden:

- **Taken ophalen**: open taken, deadlines, prioriteiten (read-only)
- **Taken aanmaken/bijwerken**: nieuwe taak aanmaken of status wijzigen
- **Activiteit ophalen**: recente updates van collega's in gedeelde spaces

Dit is nog niet gebouwd.

---

## Auth: wat je nodig hebt

**Type:** Personal API Token (eenvoudigst) of OAuth App  
**Waar aan te maken:** ClickUp → Profiel (rechtsonder) → Apps → API Token

### Stappen (eenmalig, door Lars):
1. Log in op ClickUp
2. Klik rechtsonder op je profielinitalen → Apps
3. Kopieer je **Personal API Token**
4. Optioneel: noteer je **Team ID** (workspace-ID) via de ClickUp URL of API

### Benodigde credentials:
```
CLICKUP_API_TOKEN=pk_...
CLICKUP_TEAM_ID=...       (workspace-ID, te vinden in URL of via /team endpoint)
```

**Privacy-noot:** Taken kunnen klantdata en projectdetails bevatten. Behandel als intern vertrouwelijk.

---

## Geplande scripts

### `get_taken.py`
- **Input:** space/list filter (optioneel), status filter (default: open), toegewezen aan (default: Lars)
- **Output:** JSON: `[{id, titel, status, prioriteit, deadline, lijst, toegewezen}]`

### `maak_taak.py`
- **Input:** titel, beschrijving, lijst-ID, prioriteit, deadline
- **Output:** taak-ID van aangemaakte taak
- **STOP:** vraag bevestiging als de taak aan iemand anders wordt toegewezen

### `update_taak.py`
- **Input:** taak-ID, veld (status/prioriteit/deadline), nieuwe waarde
- **Output:** bevestiging van update

### `get_activiteit.py`
- **Input:** space-ID, since (tijdstip, default: gisteren 17:00)
- **Output:** JSON met recente acties van teamleden: `[{persoon, actie, taak, tijdstip}]`
