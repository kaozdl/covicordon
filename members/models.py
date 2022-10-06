from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords

# Create your models here.
class Member(models.Model):

    first_name = models.CharField(
        max_length=128,
        verbose_name='primer nombre',
    )
    second_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='segundo nombre',
    )
    first_surname = models.CharField(
        max_length=128,
        verbose_name='primer apellido',
    )
    second_surname = models.CharField(
        max_length=128,
        verbose_name='segundo apellido',
    )
    titular = models.BooleanField(default=False)

    phone_number = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='numero de telefono'
    )
    member_number = models.SmallIntegerField(
        db_index=True,
        verbose_name='numero de socio',
    )

    bedrooms = models.SmallIntegerField(
        default=2,
        validators=[MinValueValidator(2), MaxValueValidator(4)],
        verbose_name='num dormitorios',
    )
    apartment_number = models.SmallIntegerField(
        verbose_name='numero de unidad',
    )


    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'


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
        verbose_name='tipo',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha creación',
    )

    ammount = models.FloatField(
        verbose_name='monto',
    )

    description = models.TextField(
        verbose_name='descripción',
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.member.first_name} {self.member.first_surname} {self.ammount}'

    class Meta:
        verbose_name = 'Deuda'
