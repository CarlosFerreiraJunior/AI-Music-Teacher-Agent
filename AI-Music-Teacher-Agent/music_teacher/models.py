from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


VALID_INSTRUMENTS = {"violao", "cavaquinho"}
VALID_LEVELS = {"iniciante", "intermediario", "avancado"}
VALID_OBJECTIVES = {"tirar intro", "aprender base", "entender harmonia"}


@dataclass(frozen=True)
class StudentRequest:
    instrumento: str
    nivel: str
    musica: str
    artista: str
    objetivo: str
    tempo_disponivel: int

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "StudentRequest":
        errors: list[str] = []
        required = ["instrumento", "nivel", "musica", "artista", "objetivo", "tempo_disponivel"]

        for field in required:
            if field not in payload or payload[field] in (None, ""):
                errors.append(f"Campo obrigatorio ausente: {field}")

        if errors:
            raise ValueError("; ".join(errors))

        instrumento = _normalize_text(payload["instrumento"])
        nivel = _normalize_text(payload["nivel"])
        objetivo = _normalize_text(payload["objetivo"])
        musica = str(payload["musica"]).strip()
        artista = str(payload["artista"]).strip()

        try:
            tempo_disponivel = int(payload["tempo_disponivel"])
        except (TypeError, ValueError) as exc:
            raise ValueError("tempo_disponivel deve ser um numero inteiro em minutos") from exc

        if instrumento not in VALID_INSTRUMENTS:
            errors.append("instrumento deve ser 'violao' ou 'cavaquinho'")
        if nivel not in VALID_LEVELS:
            errors.append("nivel deve ser 'iniciante', 'intermediario' ou 'avancado'")
        if objetivo not in VALID_OBJECTIVES:
            errors.append("objetivo deve ser 'tirar intro', 'aprender base' ou 'entender harmonia'")
        if tempo_disponivel < 10:
            errors.append("tempo_disponivel deve ser pelo menos 10 minutos")
        if tempo_disponivel > 180:
            errors.append("tempo_disponivel deve ser no maximo 180 minutos")

        if errors:
            raise ValueError("; ".join(errors))

        return cls(
            instrumento=instrumento,
            nivel=nivel,
            musica=musica,
            artista=artista,
            objetivo=objetivo,
            tempo_disponivel=tempo_disponivel,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _normalize_text(value: Any) -> str:
    return str(value).strip().lower()
