import json
import unittest
from pathlib import Path

from music_teacher.agents import PlannerAgent
from music_teacher.models import StudentRequest
from music_teacher.storage import save_result


class StorageTest(unittest.TestCase):
    def test_save_result_writes_json_file(self) -> None:
        request = StudentRequest.from_dict(
            {
                "instrumento": "violao",
                "nivel": "iniciante",
                "musica": "Carinhoso",
                "artista": "Pixinguinha",
                "objetivo": "aprender base",
                "tempo_disponivel": 20,
            }
        )
        result = PlannerAgent().run(request)

        output_dir = Path("outputs-test")
        destination = save_result(result, output_dir)
        payload = json.loads(Path(destination).read_text(encoding="utf-8"))

        self.assertEqual(payload["result"]["input"]["musica"], "Carinhoso")
        self.assertIn("created_at", payload)


if __name__ == "__main__":
    unittest.main()
