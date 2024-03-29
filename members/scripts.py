from members.models import Debt, Member
from movements.models import Payment


def generar_deudas():
    for member in Member.objects.all():  # Todos los socios
        cuota_social = Debt(
            member=member, type="cuota_social", ammount=gen_cuota_social(member)
        )
        gastos_comunes = Debt(
            member=member,
            type="gastos_comunes",
            ammount=VALOR_GC,
        )
        for debt in [cuota_social, gastos_comunes]:
            debt.save()
