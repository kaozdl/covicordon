from django import forms

from .models import Payment
from members.models import Member


class DateInput(forms.DateInput):
    input_type = "date"


class PaymentForm(forms.ModelForm):

    deposited_at = forms.DateField(label="Depositado", widget=DateInput)
    attachment = forms.FileField(label="Comprobante")
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label="Socio")
    ammount = forms.FloatField(label="Monto")
    reference = forms.CharField(label="Referencia")

    class Meta:
        model = Payment
        fields = ("deposited_at", "member", "attachment", "ammount", "reference")
