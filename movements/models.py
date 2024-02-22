from django.db import models
from simple_history.models import HistoricalRecords

class Account(models.Model):

    name = models.CharField(
        verbose_name='nombre',
        max_length=128,
    )
    ammount = models.FloatField(verbose_name='saldo')
    currency = models.CharField(
        max_length=128,
        verbose_name='moneda',
    )

    class Meta:
        verbose_name = 'cuenta'


class ProviderPayment(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha creacion',
    )
    ammount = models.FloatField(
        verbose_name='monto',
    )
    currency = models.CharField(
        verbose_name='moneda',
        max_length=128
    )
    description = models.TextField(
        verbose_name='descripción',
    )
    provider = models.CharField(
        max_length=128,
        verbose_name='proveedor',
    )

    class Meta:
        verbose_name = 'Pago Proveedor'
        verbose_name_plural = 'Pagos a proveedores'


