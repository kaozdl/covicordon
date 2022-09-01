from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Member, Debt



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

# Register your models here.
admin.site.register(Member)
