# Monitoring

Hoe Opus een draaiende app in de gaten houdt, en wat "verbeteren" concreet betekent.

---

## Wat Opus monitort

### 1. Health-check (elk interval X)
- Roept `/health` of equivalent aan
- Verwacht HTTP 200 en `{"status": "ok"}` (of equivalent)
- Bij fout: direct rapport aan Lars — geen autonome restart zonder bevestiging

### 2. Logs (dagelijks samenvatten)
- Foutregels (ERROR, CRITICAL, 5xx) tellen en samenvatten
- Onverwachte patronen markeren
- Geen loginhoud met klantdata doorsturen naar externe LLM

### 3. Uptime (passief)
- Bij deployment: startijd loggen
- Bij health-fout: downtime registreren in `apps/<naam>/monitoring/log.md`

### 4. Wat Opus NIET monitort (zonder expliciete opdracht)
- Performance-metrics (CPU, geheugen) — vereist extra tooling
- Gebruikersgedrag of analytics
- Database-inhoud

---

## Wat "verbeteren" concreet betekent

### Mag autonoom (level 4):
- Bugfix in logica die geen externe impact heeft, na schrijven van reproducerende test
- Dependency-update in development (niet productie)
- Refactor die gedrag niet verandert, met bestaande tests als bewijs

### Vereist STOP + akkoord Lars:
- Elke wijziging die naar productie gaat (zie DRAAIBOEK.md Fase 4)
- Nieuwe externe koppelingen of API-calls
- Wijziging in datamodel of opslag
- Verhoging van rechten of toegang
- Wijziging die logging of monitoring beïnvloedt

### Grenzen aan "verbeteren":
Opus stelt verbeteringen voor, bouwt ze voor, maar deployt ze pas na expliciete opdracht.
"Ik heb de fix klaar" betekent: lokaal getest, wacht op jouw fiat.
"Ik heb de fix gerold" mag Opus nooit zeggen zonder dat Lars de deploy heeft goedgekeurd.

---

## Rapportage

Opus rapporteert monitoring-bevindingen:
- Direct bij kritieke fout (app down, 5xx-storm)
- Dagelijks bij ochtendbriefing als er iets afwijkt
- Nooit bij "alles groen" — geen onnodige notificaties

Formaat rapport:
```
[MONITORING] apps/<naam> — <datum>
Status: ✓ OK / ✗ DOWN / ⚠ AFWIJKING
Samenvatting: <één zin>
Actie vereist: ja/nee — <wat>
```
