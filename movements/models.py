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


class ProviderPayments(models.Model):

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



class Payment(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creacion',
    )
    deposited_at = models.DateField(
        null=True,
        blank=True,
        verbose_name='fecha de depósito',
    )
    verified = models.BooleanField(
        default=False,
        blank=True,
        verbose_name='verificado'
    )
    member = models.ForeignKey(
        'members.Member',
        on_delete=models.DO_NOTHING,
        related_name='payments',
    )
    ammount = models.FloatField(
        verbose_name='monto'
    )
    attachment = models.FileField(
        verbose_name='adjunto'
    )
    reference = models.CharField(
        max_length=128,
        verbose_name='num referencia'
    )
    notes = models.TextField(
        null=True,
        blank=True,
        verbose_name='notas',
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name='Pago'
