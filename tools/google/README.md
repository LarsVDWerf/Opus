# Tool: Google

## Wat doet deze tool
Toegang tot Google Workspace via de Google APIs. Twee verantwoordelijkheden:

- **Gmail**: inbox lezen, concepten aanmaken (nooit direct versturen)
- **Google Calendar**: afspraken ophalen (read-only)

Elke verantwoordelijkheid wordt een apart script. Dit is nog niet gebouwd.

---

## Auth: wat je nodig hebt

**Type:** OAuth 2.0 via Google Cloud Console  
**Waar aan te maken:** https://console.cloud.google.com

### Stappen (eenmalig, door Lars):
1. Ga naar Google Cloud Console → nieuw project aanmaken (bijv. `opus-agent`)
2. APIs & Services → Enable APIs:
   - Gmail API
   - Google Calendar API
3. APIs & Services → Credentials → Create credentials → OAuth 2.0 Client ID
4. Application type: **Desktop app**
5. Download de `credentials.json` → bewaar als `tools/google/credentials.json` (staat in .gitignore)
6. Eerste keer draaien: browser-flow voor toestemming → genereert `token.json` (ook in .gitignore)

### Benodigde bestanden (NIET in git):
```
tools/google/credentials.json   ← gedownload uit Google Cloud Console
tools/google/token.json          ← gegenereerd bij eerste OAuth-flow
```

**Scopes die nodig zijn:**
```
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.compose
https://www.googleapis.com/auth/calendar.readonly
```

**Privacy-noot:** Gmail kan privé- én klantcommunicatie bevatten. Zie CLAUDE.md → Privacy & modelkeuze. Verwerk deze data nooit via een externe LLM zonder expliciete toestemming.

---

## Geplande scripts

### `get_agenda.py`
- **Input:** datum (default: vandaag), aantal dagen (default: 1), kalender-ID (default: `primary`)
- **Output:** JSON met lijst van afspraken: `[{tijd, titel, locatie, duur_min, deelnemers}]`

### `get_mail.py`
- **Input:** label (default: INBOX), max aantal (default: 20), ongelezen-filter (bool)
- **Output:** JSON met lijst: `[{id, afzender, onderwerp, snippet, datum, gelezen}]`

### `maak_mail_concept.py`
- **Input:** reply_op_id of nieuw, aan, onderwerp, body
- **Output:** concept-ID in Drafts; nooit direct versturen
- **STOP:** altijd concept, nooit `send=True` zonder expliciete bevestiging Lars
