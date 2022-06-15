from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import PaymentForm

# Create your views here.
class PaymentUploadView(FormView):
    template_name = 'upload_payment'
    form_class = PaymentForm
    success_url = '/'

    def form_valid(self, form):
        import ipdb; ipdb.set_trace()
        form.save()
        return super().form_valid(form)
