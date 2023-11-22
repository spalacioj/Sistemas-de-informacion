from django.db import models

class empleados(models.Model):
    Nombre = models.TextField(max_length=40)
    Numero = models.IntegerField()
    Horas = models.IntegerField()

    def __str__(self):
        return self.Nombre
    
    def get_info(self):
        return {
            'Nombre': self.Nombre,
            'Numero': self.Numero,
            'Horas': self.Horas
        }
