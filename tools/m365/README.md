# Tool: Microsoft 365

## Wat doet deze tool
Toegang tot Microsoft 365 via de Graph API. Drie verantwoordelijkheden:

- **Agenda**: afspraken van vandaag/deze week ophalen (read-only)
- **Mail**: inbox lezen, concept-replies aanmaken (nooit direct versturen)
- **Teams**: kanaalupdates en mentions ophalen (read-only)

Elke verantwoordelijkheid wordt een apart script. Dit is nog niet gebouwd.

---

## Auth: wat je nodig hebt

**Type:** OAuth 2.0 via Microsoft Graph API  
**Waar aan te maken:** Azure Portal → App registrations

### Stappen (eenmalig, door Lars):
1. Ga naar https://portal.azure.com → Azure Active Directory → App registrations → New registration
2. Geef de app een naam, bijv. `opus-agent`
3. Na aanmaken: kopieer **Application (client) ID** en **Directory (tenant) ID**
4. Ga naar Certificates & secrets → New client secret → kopieer de waarde direct (verdwijnt na verlaten pagina)
5. Ga naar API permissions → Add permission → Microsoft Graph → Delegated:
   - `Calendars.Read`
   - `Mail.Read`
   - `Mail.ReadWrite` (voor concepten)
   - `ChannelMessage.Read.All`
6. Grant admin consent

### Benodigde credentials (op te slaan in `.env` of secrets-manager):
```
M365_CLIENT_ID=...
M365_CLIENT_SECRET=...
M365_TENANT_ID=...
M365_USER_EMAIL=l.vanderwerf@univia.nl
```

**Privacy-noot:** mail en agenda kunnen klantdata bevatten. Zie CLAUDE.md → Privacy & modelkeuze. Verwerk deze data nooit via een externe LLM zonder expliciete toestemming van Lars.

---

## Geplande scripts

### `get_agenda.py`
- **Input:** datum (default: vandaag), aantal dagen (default: 1)
- **Output:** JSON met lijst van afspraken: `[{tijd, titel, locatie, duur_min, deelnemers}]`

### `get_mail.py`
- **Input:** map (default: inbox), max aantal (default: 20), ongelezen-filter (bool)
- **Output:** JSON met lijst: `[{id, afzender, onderwerp, snippet, datum, gelezen}]`

### `maak_mail_concept.py`
- **Input:** reply_op_id of nieuw, aan, onderwerp, body
- **Output:** concept-ID in Drafts; nooit direct versturen
- **STOP:** altijd concept, nooit `send=True` zonder expliciete bevestiging Lars

### `get_teams_updates.py`
- **Input:** kanalen (lijst), since (tijdstip, default: gisteren 17:00)
- **Output:** JSON met berichten en mentions
