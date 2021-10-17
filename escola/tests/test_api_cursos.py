from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from escola.models import Curso


class TestAPICursos(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso="CTT1", descricao="Curso Teste 1", nivel="B"
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso="CTT2", descricao="Curso Teste 2", nivel="A"
        )

    def test_if_list_all_courses(self):
        """Test if couses are listed correctly."""
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('codigo_curso'), 'CTT1')
        self.assertEqual(response.data[1].get('codigo_curso'), 'CTT2')

    def test_course_creation(self):
        """Should create a new course."""

        data = {
            "codigo_curso": "CTT3",
            "descricao": "Curso Teste 3",
            "nivel": "A"
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('codigo_curso'), 'CTT3')

    def test_prevent_delete_a_course(self):
        """Should return a 405 error because delete method is not allowed for courses."""
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_a_course(self):
        """Should update a course."""
        data = {
            "codigo_curso": "CTT1",
            "descricao": "Cursão meu",
            "nivel": "A"
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('descricao'), "Cursão meu")

    def test_partial_update_a_course(self):
        """Should partial update a course."""
        data = {
            "descricao": "Cursão meu",
        }
        response = self.client.patch('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('descricao'), "Cursão meu")
