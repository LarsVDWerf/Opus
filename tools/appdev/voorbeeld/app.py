"""
Voorbeeld minimale Opus-app — lokaal only, niet deployen.

Toont de vorm van wat Opus kan produceren als scaffold.
Draai met: pip install -r requirements.txt && python app.py
Bezoek: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Opus voorbeeld-app")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
      <body style="font-family: sans-serif; padding: 2rem; max-width: 600px; margin: auto">
        <h1>Opus voorbeeld-app</h1>
        <p>Dit is een minimale scaffold — de vorm die Opus gebruikt als startpunt.</p>
        <ul>
          <li><a href="/health">/health</a> — status-endpoint</li>
          <li><a href="/docs">/docs</a> — automatische API-documentatie</li>
        </ul>
        <p style="color: #888; font-size: 0.85rem">
          [LOKAAL ONLY — niet gedeployed, geen externe data]
        </p>
      </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
