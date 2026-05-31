# Voorbeeld-app

Minimale scaffold — toont de basisvorm van een Opus-gebouwde app.

**Lokaal only. Niet deployen.**

## Draaien

```bash
cd tools/appdev/voorbeeld
pip install -r requirements.txt
python app.py
```

Bezoek: http://localhost:8000

## Wat je ziet
- `/` — eenvoudige HTML-pagina
- `/health` — `{"status": "ok"}`
- `/docs` — automatische Swagger-documentatie (FastAPI)

## Dit is een scaffold, geen productie-app
Echte apps komen in `/apps/<naam>/` en volgen DRAAIBOEK.md.
