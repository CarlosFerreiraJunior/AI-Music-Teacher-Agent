import unittest

from music_teacher.agents import PlannerAgent, StudyPlanAgent
from music_teacher.models import StudentRequest


def sample_request(tempo_disponivel: int = 20) -> StudentRequest:
    return StudentRequest.from_dict(
        {
            "instrumento": "cavaquinho",
            "nivel": "intermediario",
            "musica": "O Mundo e um Moinho",
            "artista": "Cartola",
            "objetivo": "entender harmonia",
            "tempo_disponivel": tempo_disponivel,
        }
    )


class StudyPlanAgentTest(unittest.TestCase):
    def test_blocks_sum_to_available_time(self) -> None:
        request = sample_request(30)
        plan = StudyPlanAgent().run(request)

        total_blocks = sum(block["minutos"] for block in plan["blocos"])

        self.assertEqual(plan["tempo_total"], 30)
        self.assertEqual(total_blocks, 30)
        self.assertEqual([block["nome"] for block in plan["blocos"]], ["Aquecimento", "Tecnica", "Aplicacao", "Desafio"])


class PlannerAgentTest(unittest.TestCase):
    def test_planner_returns_complete_response_contract(self) -> None:
        result = PlannerAgent().run(sample_request())

        self.assertIn("fontes", result)
        self.assertIn("analise", result)
        self.assertIn("exercicios", result)
        self.assertIn("plano_estudo", result)
        self.assertGreaterEqual(len(result["fontes"]), 3)
        self.assertGreaterEqual(len(result["exercicios"]), 3)
        self.assertEqual(result["plano_estudo"]["tempo_total"], 20)


if __name__ == "__main__":
    unittest.main()
