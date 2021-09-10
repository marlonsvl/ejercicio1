from django.db import models

class ValorCambio(models.Model):
    url = models.CharField(max_length=500)
    fecha = models.DateTimeField('fecha')
    valor = models.DecimalField('valor', max_digits=5, decimal_places=2)
