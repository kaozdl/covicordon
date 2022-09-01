from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Payment, Account

@admin.register(Account)
class AccountAdmin(SimpleHistoryAdmin):

    fields = (
        'name',
        'ammount',
        'currency',
    )

    list_display = ('name', 'ammount', 'currency')
    history_list_display = ('name', 'ammount', 'currency')


# Register your models here.
@admin.register(Payment)
class PaymentAdmin(SimpleHistoryAdmin):

    fields = (
        'created_at',
        'deposited_at',
        'verified',
        'member',
        'attachment',
        'reference',
        'notes',
        'ammount',
    )

    list_display = ('member', 'created_at', 'deposited_at', 'verified', 'reference')
    history_list_display = (
        'member',
        'created_at',
        'verified',
        'ammount',
        'reference',
        'notes',
    )
    readonly_fields = ('created_at',)

    class Meta:
        model = Payment
