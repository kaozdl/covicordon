from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import PaymentForm
from .models import Payment

def success_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    return render(
        request,
        'success_payment.html',
        { 'payment': payment },
    )


def list_payments(request, start_date, end_date):
    pass


# Create your views here.
class PaymentUploadView(FormView):
    template_name = 'upload_payment'
    form_class = PaymentForm

    def get_success_url(self):
        return f'/success-payment/{self.payment.id}'

    def form_valid(self, form):
        self.payment = form.save()
        return super().form_valid(form)

