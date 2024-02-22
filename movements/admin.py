from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Account, ProviderPayment

@admin.register(Account)
class AccountAdmin(SimpleHistoryAdmin):

    fields = (
        'name',
        'ammount',
        'currency',
    )

    list_display = ('name', 'ammount', 'currency')
    history_list_display = ('name', 'ammount', 'currency')



@admin.register(ProviderPayment)
class ProviderPaymentAdmin(SimpleHistoryAdmin):

    fields = (
        'created_at',
        'currency',
        'ammount',
        'description',
        'provider',
    )

    list_display = (
        'provider',
        'ammount',
        'currency',
        'created_at',
    )
    readonly_fields = ('created_at',)
