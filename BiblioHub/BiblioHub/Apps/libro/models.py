from django.db import models

class Libro(models.Model):
        titulo= models.CharField(maxlength=100)
        autor=models.ForeignKey(
                'autor.Autor',
                on_delete=models.DO_NOTHING
        )
        genero=models.ForeignKey(
                'genero.Genero',
                on_delete=models.DO_NOTHING
        )                   
        isbn=models.BigIntegerField()
        

        def __str__(self):
                return self.titulo



