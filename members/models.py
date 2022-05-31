from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Member(models.Model):

    first_name = models.CharField(
        max_length=128,
        verbose_name=_('first_name'),
    )
    second_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_('second_name'),
    )
    first_surname = models.CharField(
        max_length=128,
        verbose_name=_('first_surname'),
    )
    second_surname = models.CharField(
        max_length=128,
        verbose_name=_('second_surname'),
    )
    titular = models.BooleanField(default=False)

    phone_number = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_('phone_number')
    )
    member_number = models.SmallIntegerField(
        db_index=True,
        verbose_name=_('member_number'),
    )

    bedrooms = models.SmallIntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(4)])

    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')


    def __str__(self):
        return f'{self.member_number} {self.first_name} {self.first_surname}'

class Debt(models.Model):

    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)

    DEBT_TYPES = (
        ('cuota_social', 'Cuota social'),
        ('gastos_comunes', 'Gastos comunes'),
        ('fondo_socorro', 'Fondo socorro'),
        ('atraso_cuota', 'Atraso cuota'),
        ('falta_asamblea', 'Falta asamblea'),
        ('falta_obra', 'Falta obra'),
        ('convenio_social', 'Convenio social'),
        ('prestamo_inacoop', 'Préstamo inacoop'),
        ('salon_comunal', 'Salon comunal'),
        ('salon_otros', 'Salon otros'),
        ('saldo_anterior', 'Saldo anterior'),
        ('otros', 'Otros'),
    )

    type = models.CharField(
        max_length=256,
        choices=DEBT_TYPES,
        verbose_name=_('type'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created_at'),
    )

    ammount = models.FloatField(
        verbose_name=_('ammount'),
    )

    description = models.TextField(
        verbose_name=_('description'),
        null=True,
        blank=True,
    )

