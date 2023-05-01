from django.db import models

# Create your models here.
class Autor(models.Model):
        titulo=models.TextField(max_length=100)

        def __str__(self):
            return self.titulo