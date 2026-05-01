from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from music_teacher.models import StudentRequest


@dataclass(frozen=True)
class Source:
    tipo: str
    titulo: str
    url: str
    relevancia: str


class SearchAgent:
    def run(self, request: StudentRequest) -> list[dict[str, str]]:
        query = f"{request.musica} {request.artista}".replace(" ", "+")
        instrument_query = request.instrumento.replace("violao", "viol%C3%A3o")
        sources = [
            Source(
                tipo="video",
                titulo=f"Busca de aulas para {request.musica} - {request.artista}",
                url=f"https://www.youtube.com/results?search_query={query}+{instrument_query}+aula",
                relevancia="alta",
            ),
            Source(
                tipo="cifra",
                titulo=f"Busca de cifras para {request.musica}",
                url=f"https://www.google.com/search?q={query}+cifra+{instrument_query}",
                relevancia="media",
            ),
            Source(
                tipo="aula",
                titulo=f"Referencias de {request.objetivo} para {request.instrumento}",
                url=f"https://www.google.com/search?q={request.objetivo.replace(' ', '+')}+{instrument_query}+samba+pagode+bossa",
                relevancia="media",
            ),
        ]
        return [asdict(source) for source in sources]


class MusicTheoryAgent:
    def run(self, request: StudentRequest) -> dict[str, Any]:
        level_notes = {
            "iniciante": "foque em reconhecer a pulsacao, trocar acordes limpos e manter a levada constante.",
            "intermediario": "observe funcoes harmonicas, antecipacoes ritmicas e pequenas variacoes de conducao.",
            "avancado": "analise substituicoes, baixos de passagem, tensoes e nuances de interpretacao.",
        }
        objective_notes = {
            "tirar intro": "isole frases curtas, cante antes de tocar e reduza a velocidade.",
            "aprender base": "priorize levada, troca de acordes e acentos caracteristicos do estilo.",
            "entender harmonia": "mapeie repouso, preparacao e tensao antes de decorar nomes de acordes.",
        }
        instrument_challenge = {
            "violao": "regularidade da mao direita e clareza nas pestanas ou acordes com extensoes.",
            "cavaquinho": "precisao da palhetada, abafamentos e troca rapida de shapes compactos.",
        }

        return {
            "resumo": (
                f"Para estudar {request.musica} de {request.artista}, trate o objetivo "
                f"'{request.objetivo}' como uma pratica guiada: {objective_notes[request.objetivo]}"
            ),
            "tom_estimado": "nao estimado automaticamente no MVP; confirme em uma fonte confiavel antes de tocar junto.",
            "progressao": "identifique primeiro os acordes de repouso e depois os acordes de passagem.",
            "linguagem_por_nivel": level_notes[request.nivel],
            "desafios": [
                instrument_challenge[request.instrumento],
                "manter andamento estavel sem acelerar nas trocas dificeis.",
                "separar estudo ritmico de estudo harmonico para evitar sobrecarga.",
            ],
        }


class TechniqueCoachAgent:
    def run(self, request: StudentRequest) -> list[dict[str, str]]:
        rhythm = "levada com polegar e dedos" if request.instrumento == "violao" else "palhetada alternada com abafamento"
        level_focus = {
            "iniciante": "bem lento, buscando som limpo",
            "intermediario": "com metronomo e pequenas variacoes",
            "avancado": "com dinamica, acentos deslocados e andamento proximo ao original",
        }
        objective_focus = {
            "tirar intro": "fraseado em blocos de 2 compassos",
            "aprender base": "ciclo de acordes e levada",
            "entender harmonia": "funcoes dos acordes e conducoes de baixo",
        }

        return [
            {
                "nome": "Pulso e subdivisao",
                "foco": f"Marcar tempo e contratempo antes de tocar a musica; {level_focus[request.nivel]}.",
                "duracao_sugerida": "3-5 min",
            },
            {
                "nome": f"Tecnica de {request.instrumento}",
                "foco": f"Praticar {rhythm} com acordes simples da musica.",
                "duracao_sugerida": "5-8 min",
            },
            {
                "nome": f"Aplicacao: {objective_focus[request.objetivo]}",
                "foco": "Usar um trecho curto da musica e repetir ate soar musical, nao apenas correto.",
                "duracao_sugerida": "7-12 min",
            },
        ]


class StudyPlanAgent:
    def run(self, request: StudentRequest) -> dict[str, Any]:
        total = request.tempo_disponivel
        warmup = max(2, round(total * 0.2))
        technique = max(3, round(total * 0.35))
        application = max(3, round(total * 0.3))
        challenge = total - warmup - technique - application

        if challenge < 2:
            application -= 2 - challenge
            challenge = 2

        blocks = [
            {"nome": "Aquecimento", "minutos": warmup, "atividade": "pulso, troca lenta de acordes e som limpo."},
            {"nome": "Tecnica", "minutos": technique, "atividade": "exercicio principal adaptado ao instrumento."},
            {"nome": "Aplicacao", "minutos": application, "atividade": "trecho curto da musica com foco no objetivo."},
            {"nome": "Desafio", "minutos": challenge, "atividade": "tocar sem parar e anotar o ponto mais instavel."},
        ]

        return {"tempo_total": total, "blocos": blocks}


class PlannerAgent:
    def __init__(
        self,
        search_agent: SearchAgent | None = None,
        theory_agent: MusicTheoryAgent | None = None,
        coach_agent: TechniqueCoachAgent | None = None,
        plan_agent: StudyPlanAgent | None = None,
    ) -> None:
        self.search_agent = search_agent or SearchAgent()
        self.theory_agent = theory_agent or MusicTheoryAgent()
        self.coach_agent = coach_agent or TechniqueCoachAgent()
        self.plan_agent = plan_agent or StudyPlanAgent()

    def run(self, request: StudentRequest) -> dict[str, Any]:
        return {
            "input": request.to_dict(),
            "fontes": self.search_agent.run(request),
            "analise": self.theory_agent.run(request),
            "exercicios": self.coach_agent.run(request),
            "plano_estudo": self.plan_agent.run(request),
            "observacoes": [
                "MVP nao copia cifras ou partituras completas; use os links como referencia externa.",
                "Confirme tom e acordes na fonte escolhida antes de tocar junto com a gravacao original.",
            ],
        }
