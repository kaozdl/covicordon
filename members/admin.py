from django.contrib import admin
from .models import Member, Debt

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
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

# Register your models here.
admin.site.register(Member)
