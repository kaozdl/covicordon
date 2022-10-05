from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Member, Debt
from members.constants import VALOR_GC, VALOR_INACOOP, VALOR_UR, gen_cuota_social

@admin.action(description='generar deuda para socios seleccionados')
def generate_debt(modeladmin, request, queryset):
    for member in queryset:
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


@admin.register(Member)
class MemberAdmin(SimpleHistoryAdmin):
    list_display = [
        'member_number',
        'first_name',
        'first_surname',
    ]

    actions = [generate_debt]




@admin.register(Debt)
class DebtAdmin(SimpleHistoryAdmin):
    list_display = [
        'member',
        'type',
        'ammount',
        'created_at',
    ]

    sortable_by = [
        'member',
        'type',
        'created_at',
    ]

    list_filter = [
        'member',
        'type',
    ]
