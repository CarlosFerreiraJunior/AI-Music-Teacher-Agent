from __future__ import annotations

from typing import Any


def result_to_markdown(result: dict[str, Any]) -> str:
    request = result["input"]
    lines = [
        f"# Plano de Estudo - {request['musica']} ({request['artista']})",
        "",
        f"- Instrumento: {request['instrumento']}",
        f"- Nivel: {request['nivel']}",
        f"- Objetivo: {request['objetivo']}",
        f"- Tempo disponivel: {request['tempo_disponivel']} min",
        "",
        "## Fontes",
    ]

    for source in result["fontes"]:
        lines.append(f"- [{source['tipo']}] {source['titulo']} ({source['relevancia']}): {source['url']}")

    analysis = result["analise"]
    lines.extend(
        [
            "",
            "## Analise Musical",
            "",
            analysis["resumo"],
            "",
            f"- Tom estimado: {analysis['tom_estimado']}",
            f"- Progressao: {analysis['progressao']}",
            f"- Foco por nivel: {analysis['linguagem_por_nivel']}",
            "",
            "### Desafios",
        ]
    )
    lines.extend(f"- {challenge}" for challenge in analysis["desafios"])

    lines.extend(["", "## Exercicios"])
    for exercise in result["exercicios"]:
        lines.append(f"- {exercise['nome']} ({exercise['duracao_sugerida']}): {exercise['foco']}")

    plan = result["plano_estudo"]
    lines.extend(["", f"## Plano de Estudo ({plan['tempo_total']} min)"])
    for index, block in enumerate(plan["blocos"], start=1):
        lines.append(f"{index}. {block['nome']} ({block['minutos']} min): {block['atividade']}")

    lines.extend(["", "## Observacoes"])
    lines.extend(f"- {note}" for note in result["observacoes"])
    return "\n".join(lines)
