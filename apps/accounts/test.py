from django.test import TestCase
from apps.accounts.models import Carrera, Materia


class AccountsTest(TestCase):
    def crear_carrera(self):
        carrera = Carrera(
            nombre='Ingeniería en sistemas computacionales',
        )
        carrera.save()

    def create_materia(self):
        materia = Materia(
            nombre='Ingeniería de software',
            competencia='Desarrolla soluciones de software, considerando' +
            'la metodología y herramientas para la elaboración de un ' +
            'proyecto aplicativo en diferentes escenarios.',
            clave_materia='SCD-1011',
        )
        materia.save()
