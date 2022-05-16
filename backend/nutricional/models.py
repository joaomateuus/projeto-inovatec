from django.db import models
from cardapio.models import Prato

class Nutricional(models.Model):
    
    prato = models.OneToOneField(
        Prato, on_delete=models.CASCADE, null=True, blank=True)
    valorEnergetico = models.DecimalField(max_digits=5, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2)
    proteinas = models.DecimalField(max_digits=5, decimal_places=2)
    gordurasTotais = models.DecimalField(max_digits=5, decimal_places=2)
    gordurasSaturadas = models.DecimalField(max_digits=5, decimal_places=2)
    gordurasTrans = models.DecimalField(max_digits=5, decimal_places=2)
    fibraAlimentar = models.DecimalField(max_digits=5, decimal_places=2)
    sodio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.prato)
