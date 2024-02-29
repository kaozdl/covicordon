from django.shortcuts import render

from .models import Debt


def invoice(request, debt_id):

    debt = Debt.objects.get(id=debt_id)
    context = {
        "debt": debt,
        "lines": debt.lines.all(),
        "member": debt.member,
        "total": debt.total,
    }

    return render(request, "invoice.html", context=context)
