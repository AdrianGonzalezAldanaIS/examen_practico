from django.db import models


# Create your models here.
class Tarea(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_registro = models.DateField()
    
    def __str__(self):
        return self.titulo