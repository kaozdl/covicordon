from django.contrib import admin
from django.forms.models import inlineformset_factory

from simple_history.admin import SimpleHistoryAdmin

from .models import Member, Debt, DebtLine, Config, Payment
from members.constants import gen_cuota_social


@admin.action(description="generar deuda para socios seleccionados")
def generate_debt(modeladmin, request, queryset):

    config = Config.get_config()

    for member in queryset:

        month_debt = Debt(member=member)
        month_debt.save()
        cuota_social = DebtLine(
            member=member,
            type="cuota_social",
            ammount=gen_cuota_social(member),
            debt=month_debt,
        )
        gastos_comunes = DebtLine(
            member=member,
            type="gastos_comunes",
            ammount=config.gc,
            debt=month_debt,
        )
        for debt in [cuota_social, gastos_comunes]:
            debt.save()


@admin.register(Payment)
class PaymentAdmin(SimpleHistoryAdmin):

    list_display = [
        "deposited_at",
        "member",
        "ammount",
        "verified",
    ]


@admin.register(Member)
class MemberAdmin(SimpleHistoryAdmin):
    list_display = [
        "member_number",
        "first_name",
        "last_name",
    ]

    actions = [generate_debt]


@admin.register(DebtLine)
class DebtLineAdmin(SimpleHistoryAdmin):
    list_display = [
        "member",
        "type",
        "ammount",
        "created_at",
    ]

    sortable_by = [
        "member",
        "type",
        "created_at",
    ]

    list_filter = [
        "member",
        "type",
    ]


class DebtLineInline(admin.StackedInline):
    model = DebtLine
    extra = 0


@admin.register(Debt)
class DebtAdmin(SimpleHistoryAdmin):
    list_display = [
        "member",
        "total",
    ]

    inlines = [DebtLineInline]


admin.site.register(Config)
