from django.db import models


class Genero(models.Model):
    titulo=models.TextField(maxlength=100)
    autor=models.ForeignKey(
            'genero.Genero',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.titulo
