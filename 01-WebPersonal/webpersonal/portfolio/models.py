from turtle import up
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    link = models.URLField(verbose_name = "URL", null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación") # Es solo al crearse (añade hora)
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición") # Actualiza fecha y hora cuando se actualiza

    class Meta: # Metadatos expandidos
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # Fecha de creación

    def __str__(self):
        return str(self.title)