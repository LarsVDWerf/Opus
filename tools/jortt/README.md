# Tool: Jortt

## Wat doet deze tool
Read-only toegang tot Jortt voor financieel overzicht. Twee verantwoordelijkheden:

- **Facturen inzien**: openstaande facturen, recente betalingen
- **Financieel overzicht**: BTW-aangifte status, winst/verlies samenvatting

**Schrijfacties (facturen aanmaken, betalingen verwerken) zijn uit scope.**  
Zie CLAUDE.md → Autonomie: "Nooit: betalingen uitvoeren · contracten tekenen."

Dit is nog niet gebouwd.

---

## Auth: wat je nodig hebt

**Type:** Jortt API Key (OAuth 2.0 Client Credentials)  
**Waar aan te maken:** Jortt → Instellingen → Koppelingen → API

### Stappen (eenmalig, door Lars):
1. Log in op Jortt
2. Ga naar Instellingen → Koppelingen → API
3. Maak een nieuwe API-applicatie aan
4. Noteer **Client ID** en **Client Secret**
5. Base URL: `https://app.jortt.nl/oauth/token` (token), `https://api.jortt.nl` (data)

### Benodigde credentials:
```
JORTT_CLIENT_ID=...
JORTT_CLIENT_SECRET=...
```

**Privacy-noot:** Financiële data is strikt vertrouwelijk. Nooit via externe LLM verwerken. Lokale route verplicht.

---

## Geplande scripts

### `get_facturen.py`
- **Input:** status filter (default: openstaand), periode (optioneel)
- **Output:** JSON: `[{id, klant, bedrag, vervaldatum, status}]`
- **Read-only**

### `get_financieel_overzicht.py`
- **Input:** periode (default: huidige maand/kwartaal)
- **Output:** JSON met totalen: `{omzet, kosten, winst, btw_te_betalen}`
- **Read-only**
