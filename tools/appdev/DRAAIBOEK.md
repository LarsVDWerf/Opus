# App-dev Draaiboek

Dit is het script dat Opus volgt wanneer Lars zegt "bouw die app".
Elke stap is concreet. Elke STOP is een punt waar actie van Lars vereist is.

---

## Fase 1 — Idee naar specificatie

**Opus doet:**
1. Stelt 5 vragen: wat doet de app, wie gebruikt hem, wat zijn de inputs/outputs, zijn er gevoelige data, waar moet hij draaien?
2. Schrijft een beknopte spec in `apps/<naam>/SPEC.md`: doel, gebruikers, datamodel (schets), tech-keuze, deploy-route
3. Legt de spec voor aan Lars

**→ STOP #1: Lars keurt de spec goed of past hem aan.**
*Opus handelt niet verder zonder expliciete "akkoord" op de spec.*

---

## Fase 2 — Scaffold

**Opus doet:**
1. Maakt de mapstructuur aan in `apps/<naam>/`
2. Schrijft minimale boilerplate: `app.py` / `main.py`, `requirements.txt`, `.env.example`, `README.md`
3. Draait de app lokaal: `python app.py` of `docker-compose up`
4. Verifieert dat de health-endpoint reageert (`/health` of equivalent)

**Geen externe verbindingen, geen echte data, geen credentials in deze fase.**

**→ STOP #2: Lars ziet de scaffold draaien en geeft fiat voor doorontwikkeling.**

---

## Fase 3 — Doorontwikkeling

**Opus doet:**
- Bouwt features iteratief, één per keer
- Test elke feature lokaal
- Schrijft unit-test per nieuwe functie (pytest of equivalent)
- Markeert AVG-gevoelige logica expliciet met `# AVG-GEVOELIG` commentaar

**→ STOP #3 (per feature met externe data): Lars keurt datamodel en privacyaanpak goed.**

*Bij twijfel of iets gevoelig is: stop, vraag, ga dan pas verder.*

---

## Fase 4 — Review door Lars

**Opus doet:**
1. Maakt een overzicht: wat is gebouwd, wat werkt, wat nog niet, bekende risico's
2. Draait de app lokaal zodat Lars hem zelf kan testen
3. Legt open keuzes voor (bijv. authenticatie, rate limiting, logging)

**→ STOP #4: Lars doet handmatige review. Geen deploy zonder groen licht hier.**

*Code naar productie altijd met menselijke check — zie CLAUDE.md.*

---

## Fase 5 — Deploy

**Opus doet:**
1. Voert de deploy-stappen uit volgens DEPLOY_OPTIES.md (gekozen route)
2. Verifieert dat de app bereikbaar is op het verwachte adres
3. Controleert logs direct na deploy op errors

**→ STOP #5: vereiste credentials van Lars (zie DEPLOY_OPTIES.md per route).**

**→ STOP #6: Lars bevestigt dat de live app correct werkt.**

*Opus deployt nooit autonoom naar productie. Altijd expliciete opdracht.*

---

## Fase 6 — Monitoren

Zie MONITORING.md voor de volledige aanpak.

**Opus doet na deploy:**
- Draait `check_health.py` periodiek (cron of watcher)
- Rapporteert afwijkingen proactief aan Lars

**→ STOP #7 (bij kritieke fout in productie): altijd Lars waarschuwen voor actie.**

---

## Fase 7 — Verbeteren

**Opus doet:**
- Stelt verbeteringen voor op basis van monitoring-data
- Bouwt verbetering alleen na akkoord van Lars (terug naar Fase 3)

**→ STOP #8: elke productie-wijziging start opnieuw bij Fase 4 (review).**

---

## Wat Opus nooit autonoom doet
- Productie-database migraties uitvoeren
- Secrets of credentials aanpassen
- Externe diensten koppelen zonder expliciete opdracht
- Bestaande productie-code overschrijven zonder review
