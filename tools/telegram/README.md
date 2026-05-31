# Tool: Telegram

## Wat doet deze tool
Telegram-integratie via een Telegram Bot. Twee verantwoordelijkheden:

- **Berichten ontvangen**: inkomende berichten van Lars lezen (triggers voor Opus)
- **Berichten sturen**: altijd als concept presenteren, nooit direct versturen zonder bevestiging

**Zie CLAUDE.md → Autonomie: "Altijd concept, nooit direct: Telegram"**

Dit is nog niet gebouwd.

---

## Auth: wat je nodig hebt

**Type:** Telegram Bot Token via BotFather  
**Waar aan te maken:** Telegram → zoek `@BotFather`

### Stappen (eenmalig, door Lars):
1. Open Telegram → zoek `@BotFather` → start chat
2. Stuur `/newbot` → geef een naam (bijv. `Opus`) en gebruikersnaam (bijv. `opus_lars_bot`)
3. BotFather geeft een **Bot Token** terug: `1234567890:ABCdef...`
4. Optioneel: stuur `/setprivacy` om in te stellen dat de bot alleen directe berichten verwerkt

### Chat ID ophalen (voor Lars-specifiek kanaal):
1. Stuur een bericht naar je nieuwe bot
2. Ga naar `https://api.telegram.org/bot<TOKEN>/getUpdates`
3. Noteer je **chat_id** uit de response

### Benodigde credentials:
```
TELEGRAM_BOT_TOKEN=...
TELEGRAM_LARS_CHAT_ID=...    (jouw persoonlijke chat-ID met de bot)
```

**Privacy-noot:** Telegram-berichten kunnen privécommunicatie bevatten. Altijd als concept aanbieden; Lars bepaalt of en wat er verstuurd wordt.

---

## Geplande scripts

### `ontvang_berichten.py`
- **Input:** polling-interval of webhook-URL
- **Output:** JSON met berichten: `[{id, tekst, datum, chat_id}]`
- Triggert Opus-pipeline op basis van berichtinhoud

### `maak_bericht_concept.py`
- **Input:** chat_id, tekst
- **Output:** concept-tekst getoond aan Lars — wacht op bevestiging
- **STOP:** nooit `bot.send_message()` aanroepen zonder expliciete `bevestigd=True`

### `stuur_bericht.py`
- **Input:** chat_id, tekst, bevestigd (bool — MOET True zijn)
- **Output:** bevestiging van verzending
- **STOP:** gooit fout als `bevestigd != True`
