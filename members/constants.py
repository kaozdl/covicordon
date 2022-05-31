from .models import Debt, Member

VALOR_UR = 1358
VALOR_GC = 3000
COSTO_CUARTO_UR = 2.965 # UNIDADES REAJUSTABLES
FONDO_MANTENIMIENTO = 0.42 # UNIDADES REAJUSTABLES
VALOR_INACOOP = 754


def gen_cuota_social(socio):
    return VALOR_UR * ((COSTO_CUARTO_UR * socio.bedrooms) + FONDO_MANTENIMIENTO)


def generar_deudas():
    for member in Member.objects.all(): # Todos los socios
        cuota_social = Debt(
            member=member,
            type='cuota_social',
            ammount=gen_cuota_social(member)
        )
        gastos_comunes = Debt(
            member=member,
            type='gastos_comunes',
            ammount=VALOR_GC,
        )
        inacoop = Debt(
            member=member,
            type='prestamo_inacoop',
            ammount=VALOR_INACOOP,
        )
        for debt in [cuota_social, gastos_comunes, inacoop]:
            debt.save()

