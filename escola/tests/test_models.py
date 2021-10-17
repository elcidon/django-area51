from datetime import datetime

from django.test import TestCase
from escola.models import Curso, Aluno


class CursoModelTestCase(TestCase):

    def setUp(self):
        self.curso = Curso.objects.create(
            codigo_curso="CTT1", descricao="Curso Teste 1", nivel="B"
        )

    def test_if_str_representation_returns_correctly(self):
        """Should return the correct string representation of model."""
        self.assertEqual(str(self.curso), "Curso Teste 1")


class AlunoModelTestCase(TestCase):

    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome="Erick Bruno",
            rg="000000000",
            cpf="00000000000",
            data_nascimento=datetime(1993, 5, 10),
            celular="4100000000",
        )

    def test_if_str_representation_returns_correctly(self):
        """Should return the correct string representation of model."""
        self.assertEqual(str(self.aluno), "Erick Bruno")
