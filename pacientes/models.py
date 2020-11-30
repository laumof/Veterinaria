from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    situation = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)
    dpi = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    admissionDate = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    departureDate = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)


    def __str__(self):
        return self.name
