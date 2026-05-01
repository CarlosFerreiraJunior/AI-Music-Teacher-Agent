from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from music_teacher.agents import PlannerAgent
from music_teacher.formatters import result_to_markdown
from music_teacher.models import StudentRequest
from music_teacher.storage import save_result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI Music Teacher Agent MVP")
    parser.add_argument("--input-json", help="Caminho para arquivo JSON com o input estruturado.")
    parser.add_argument("--instrumento", choices=["violao", "cavaquinho"])
    parser.add_argument("--nivel", choices=["iniciante", "intermediario", "avancado"])
    parser.add_argument("--musica")
    parser.add_argument("--artista")
    parser.add_argument("--objetivo", choices=["tirar intro", "aprender base", "entender harmonia"])
    parser.add_argument("--tempo-disponivel", type=int)
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--no-save", action="store_true", help="Nao salva o resultado em JSON.")
    parser.add_argument("--json", action="store_true", help="Imprime a resposta final em JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        payload = _load_payload(args)
        request = StudentRequest.from_dict(payload)
        result = PlannerAgent().run(request)
    except ValueError as exc:
        parser.error(str(exc))
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result_to_markdown(result))

    if not args.no_save:
        destination = save_result(result, args.output_dir)
        print(f"\nResultado salvo em: {destination}")

    return 0


def _load_payload(args: argparse.Namespace) -> dict[str, Any]:
    if args.input_json:
        path = Path(args.input_json)
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise ValueError(f"Arquivo de input nao encontrado: {path}") from exc
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON invalido em {path}: {exc}") from exc

    return {
        "instrumento": args.instrumento,
        "nivel": args.nivel,
        "musica": args.musica,
        "artista": args.artista,
        "objetivo": args.objetivo,
        "tempo_disponivel": args.tempo_disponivel,
    }


if __name__ == "__main__":
    raise SystemExit(main())
