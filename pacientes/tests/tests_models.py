from django.contrib.auth.models import User
from django.test import TestCase
from pacientes.models import Paciente

class PacienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        name = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Paciente.objects.create(name = name, size = 'Tamaño',
                                   description = 'Texto de prueba')
        pass


    def test_size_label(self):
        paciente=Paciente.objects.get(id=1)
        field_label = Paciente._meta.get_field('texto').verbose_name
        self.assertEquals(field_label,'texto')

    def test_size_max_length(self):
        paciente=Paciente.objects.get(id=1)
        max_length = Paciente._meta.get_field('tamaño').max_length
        self.assertEquals(max_length,100)
