"""Просить безкоштовну модель OpenRouter придумати слогани й описи за brief.md."""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE = Path(__file__).parent
API = "https://openrouter.ai/api/v1"

TASK = (
    "Ось бриф бізнесу «KOGRA». Придумай 5 коротких слоганів, а для кожної "
    "послуги з брифу — опис в 1–2 речення. Ціни не вигадуй, бери тільки з брифу."
)


def load_key() -> str:
    for line in (BASE / ".env").read_text(encoding="utf-8").splitlines():
        name, _, value = line.partition("=")
        if name.strip() == "OPENROUTER_API_KEY" and value.strip():
            return value.strip().strip('"').strip("'")
    sys.exit("У .env немає заповненого OPENROUTER_API_KEY")


def request(url: str, key: str | None = None, body: dict | None = None) -> dict:
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def free_models() -> list[str]:
    """Безкоштовні текстові моделі: у id є ':free'."""
    models = request(f"{API}/models")["data"]
    return [m["id"] for m in models if m["id"].endswith(":free")]


def main() -> None:
    key = load_key()
    brief = (BASE / "brief.md").read_text(encoding="utf-8")
    prompt = f"{TASK}\n\n---\n{brief}"

    # Якщо модель вказано в командному рядку — беремо тільки її, інакше пробуємо по черзі.
    models = sys.argv[1:2] or free_models()[:10]
    for model in models:
        print(f"Пробую модель: {model}", file=sys.stderr)
        try:
            raw = request(
                f"{API}/chat/completions",
                key,
                {"model": model, "messages": [{"role": "user", "content": prompt}]},
            )
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"  не вийшло: {e}", file=sys.stderr)
            continue
        text = (raw.get("choices") or [{}])[0].get("message", {}).get("content")
        if not text:
            print(f"  порожня відповідь: {json.dumps(raw)[:200]}", file=sys.stderr)
            continue

        print("=== СИРИЙ JSON ВІД СЕРВЕРА ===")
        print(json.dumps(raw, ensure_ascii=False, indent=2))
        print("\n=== ВІДПОВІДЬ МОДЕЛІ ===")
        print(text)
        return

    sys.exit("Жодна безкоштовна модель не відповіла")


if __name__ == "__main__":
    main()
