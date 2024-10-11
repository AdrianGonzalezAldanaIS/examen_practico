from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=255)  # Campo para el nombre del autor
    fecha_nacimiento = models.DateField()      # Campo para la fecha de nacimiento

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=255)          # Campo para el título del libro
    autores = models.ManyToManyField(Autor)            # Relación muchos a muchos con autores
    fecha_publicacion = models.DateField()             # Campo para la fecha de publicación

    def __str__(self):
        return self.titulo












