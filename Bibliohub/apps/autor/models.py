from django.db import models

class Autor(models.Model):
    nombre= models.TextField(max_length=100)
    
    def __str__(self):
        return self.nombre

