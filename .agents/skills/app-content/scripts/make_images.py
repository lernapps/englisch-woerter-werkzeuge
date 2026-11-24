#!/usr/bin/env python3
"""Erzeugt die Bilder von src/images/: der Werkzeugkoffer (werkzeugkoffer-1..5.svg).

Aufruf im Ordner der App: python3 .agents/skills/app-content/scripts/make_images.py
Ein neues Bild: Funktion ergänzen und starten, nie die SVG von Hand ändern.
"""
from pathlib import Path

OUT = Path("src/images")
TOOLS = ["Umschreiben", "Wortfamilie", "Teilchen", "Warnschild", "Vergleichsregel"]
COLOURS = ["#2c6fd8", "#138d75", "#d35400", "#b03a2e", "#7d3c98"]


def koffer(n: int) -> str:
    rows = []
    for i, name in enumerate(TOOLS):
        y = 70 + i * 44
        if i < n:
            rows.append(
                f'<rect x="60" y="{y}" width="360" height="36" rx="8" fill="{COLOURS[i]}"/>'
                f'<text x="80" y="{y + 25}" font-size="18" font-family="sans-serif" fill="#ffffff">{i + 1}  {name}</text>'
            )
        else:
            rows.append(
                f'<rect x="60" y="{y}" width="360" height="36" rx="8" fill="none" stroke="#6b6b6b" stroke-width="2" stroke-dasharray="6 4"/>'
                f'<text x="80" y="{y + 25}" font-size="18" font-family="sans-serif" fill="#6b6b6b">{i + 1}  noch leer</text>'
            )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 350" role="img">'
        '<rect width="480" height="350" fill="#f4efe2"/>'
        '<path d="M180 50 v-18 a10 10 0 0 1 10 -10 h100 a10 10 0 0 1 10 10 v18" fill="none" stroke="#5d4037" stroke-width="8"/>'
        '<rect x="30" y="50" width="420" height="250" rx="16" fill="#e0c9a6" stroke="#5d4037" stroke-width="4"/>'
        + "".join(rows)
        + "</svg>\n"
    )


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n in range(1, 6):
        (OUT / f"werkzeugkoffer-{n}.svg").write_text(koffer(n), encoding="utf-8")
