from django.contrib import admin

from .models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    fields = (
        'created_at',
        'deposited_at',
        'verified',
        'member',
        'attachment',
    )

    list_display = ('member', 'created_at', 'deposited_at', 'verified')
    readonly_fields = ('created_at',)

    class Meta:
        model = Payment
