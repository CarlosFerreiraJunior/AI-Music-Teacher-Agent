from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def save_result(result: dict[str, Any], output_dir: str | Path = "outputs") -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    music = _slugify(result["input"]["musica"])
    filename = f"{timestamp}-{music}.json"
    destination = output_path / filename

    payload = {
        "created_at": timestamp,
        "result": result,
    }
    destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return destination


def _slugify(value: str) -> str:
    normalized = "".join(char.lower() if char.isalnum() else "-" for char in value)
    parts = [part for part in normalized.split("-") if part]
    return "-".join(parts) or "estudo"
