from django.db import models
from apps.utils.models import Persona

class Cliente(Persona):

    def __str__(self):
        algo = super().__str__()
        return f'Cliente: {algo}'
