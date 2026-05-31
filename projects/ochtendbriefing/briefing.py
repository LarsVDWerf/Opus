#!/usr/bin/env python3
"""
Opus ochtendbriefing — werkende pipeline op mockdata.

Structuur: data ophalen → samenvoegen → één LLM-call → één alinea output.
Alle bronnen zijn MOCK. Echte integraties komen via tools/<domein>/.

Gebruik:
    python briefing.py              # mock-data + mock-LLM (standaard)
    OPUS_MOCK_LLM=false python briefing.py  # mock-data + echte LLM (vereist ANTHROPIC_API_KEY)
"""

import json
import os
import sys
from pathlib import Path

MOCK_DATA = Path(__file__).parent / "mock_data"
PROMPT_FILE = Path(__file__).parent / "prompt.md"


# ── Stap 1: data ophalen ──────────────────────────────────────────────────────

def haal_agenda_op() -> dict:
    # TODO: echte bron → tools/m365/get_agenda.py of tools/google/get_agenda.py
    with open(MOCK_DATA / "agenda.json", encoding="utf-8") as f:
        return json.load(f)


def haal_taken_op() -> dict:
    # TODO: echte bron → tools/clickup/get_taken.py
    with open(MOCK_DATA / "taken.json", encoding="utf-8") as f:
        return json.load(f)


def haal_code_activiteit_op() -> dict:
    # TODO: echte bron → git log op geconfigureerde repos (zie code_activiteit.json)
    with open(MOCK_DATA / "code_activiteit.json", encoding="utf-8") as f:
        return json.load(f)


def haal_collega_updates_op() -> dict:
    # TODO: echte bron → tools/clickup/get_activiteit.py + tools/m365/get_teams_updates.py
    with open(MOCK_DATA / "collega_updates.json", encoding="utf-8") as f:
        return json.load(f)


# ── Stap 2: samenvoegen ───────────────────────────────────────────────────────

def samenvoegen(agenda: dict, taken: dict, code: dict, collega: dict) -> dict:
    open_taken = [t for t in taken["taken"] if t["status"] == "open"]
    hoge_prio = [t for t in open_taken if t["prioriteit"] == "hoog"]

    return {
        "datum": agenda["datum"],
        "afspraken": agenda["afspraken"],
        "open_taken_aantal": len(open_taken),
        "hoge_prioriteit_taken": hoge_prio,
        "code_commits_vannacht": code["commits"],
        "open_prs": code.get("open_pull_requests", 0),
        "ci_status": code.get("CI_status", "onbekend"),
        "collega_samenvatting": collega["samenvatting"],
        "collega_updates": collega["updates"],
        "blokkades": collega.get("blokkades", []),
    }


# ── Stap 3: één LLM-call aan het eind ────────────────────────────────────────

def genereer_briefing(context: dict) -> str:
    mock_llm = os.getenv("OPUS_MOCK_LLM", "true").lower() != "false"

    if mock_llm:
        return _mock_briefing(context)
    return _echte_briefing(context)


def _mock_briefing(context: dict) -> str:
    """[MOCK — geen echte AI-call. Structureel identiek aan echte output.]"""
    afspraken = context["afspraken"]
    eerste = afspraken[0] if afspraken else None
    commits = context["code_commits_vannacht"]
    hoog = context["hoge_prioriteit_taken"]

    eerste_str = f"om {eerste['tijd']} ({eerste['titel']})" if eerste else "geen afspraken"
    hoog_str = ", ".join(t["titel"] for t in hoog) if hoog else "geen"
    commits_str = f"{len(commits)} commit{'s' if len(commits) != 1 else ''}" if commits else "geen commits"

    return (
        f"Goedemorgen. Vandaag {len(afspraken)} afspraken, eerste {eerste_str}. "
        f"{context['open_taken_aantal']} open taken, hoge prioriteit: {hoog_str}. "
        f"Vannacht {commits_str} — CI is {context['ci_status']}. "
        f"{context['collega_samenvatting']}"
    )


def _echte_briefing(context: dict) -> str:
    """Echte LLM-call via Anthropic SDK."""
    # OPEN VRAAG: zie OPEN_VRAGEN.md #1 — modelkeuze en privacy-route voor ochtendbriefing
    try:
        import anthropic
    except ImportError:
        print("FOUT: Anthropic SDK niet geïnstalleerd. Run: pip install anthropic", file=sys.stderr)
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("FOUT: ANTHROPIC_API_KEY niet gevonden. Zet OPUS_MOCK_LLM=true voor mock-modus.", file=sys.stderr)
        sys.exit(1)

    prompt = PROMPT_FILE.read_text(encoding="utf-8")
    data_blok = json.dumps(context, indent=2, ensure_ascii=False)

    client = anthropic.Anthropic(api_key=api_key)

    # TODO: vervang model na beslissing in OPEN_VRAGEN.md #1
    # Haiku voor niet-gevoelig / lokaal model voor gevoelige agenda-items
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"{prompt}\n\nDATA:\n{data_blok}"
        }]
    )

    return message.content[0].text.strip()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    mock_llm = os.getenv("OPUS_MOCK_LLM", "true").lower() != "false"

    print("[OPUS OCHTENDBRIEFING]")
    if mock_llm:
        print("[MOCK DATA + MOCK LLM — geen echte bronnen actief]")
    else:
        print("[MOCK DATA + ECHTE LLM]")
    print()

    agenda = haal_agenda_op()
    taken = haal_taken_op()
    code = haal_code_activiteit_op()
    collega = haal_collega_updates_op()

    context = samenvoegen(agenda, taken, code, collega)
    briefing = genereer_briefing(context)

    print(briefing)
    print()

    if mock_llm:
        print("─" * 60)
        print("Zet OPUS_MOCK_LLM=false + ANTHROPIC_API_KEY voor echte AI-output.")
        print("Zie OPEN_VRAGEN.md voor beslissingen die eerst nodig zijn.")


if __name__ == "__main__":
    main()
