
from django.db import models

class Campo(models.Model):
    nome = models.CharField(max_length=100)
    valor_1h = models.DecimalField(max_digits=6, decimal_places=2)
    valor_1h30 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome