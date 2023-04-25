from django.db import models

class Libro(models.Model):
    nombre= models.TextField(max_length=100)
    autor= models.ForeignKey(
        'autor.Autor', 
        on_delete=models.DO_NOTHING
    )
    genero= models.ForeignKey(
        'genero.Genero',
        on_delete=models.DO_NOTHING
    )
    isbn= models.BigIntegerField()

    borrado= models.BooleanField(default=False)

    disponible= models.BooleanField(default=True)


    def __str__(self):
        return self.libro