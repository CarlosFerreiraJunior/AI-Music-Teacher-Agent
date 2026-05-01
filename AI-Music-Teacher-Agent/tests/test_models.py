import unittest

from music_teacher.models import StudentRequest


class StudentRequestTest(unittest.TestCase):
    def test_validates_and_normalizes_payload(self) -> None:
        request = StudentRequest.from_dict(
            {
                "instrumento": " Violao ",
                "nivel": "Iniciante",
                "musica": "Samba de Uma Nota So",
                "artista": "Tom Jobim",
                "objetivo": "Aprender Base",
                "tempo_disponivel": "20",
            }
        )

        self.assertEqual(request.instrumento, "violao")
        self.assertEqual(request.nivel, "iniciante")
        self.assertEqual(request.objetivo, "aprender base")
        self.assertEqual(request.tempo_disponivel, 20)

    def test_rejects_invalid_payload(self) -> None:
        with self.assertRaisesRegex(ValueError, "instrumento"):
            StudentRequest.from_dict(
                {
                    "instrumento": "baixo",
                    "nivel": "iniciante",
                    "musica": "Teste",
                    "artista": "Teste",
                    "objetivo": "aprender base",
                    "tempo_disponivel": 20,
                }
            )


if __name__ == "__main__":
    unittest.main()
