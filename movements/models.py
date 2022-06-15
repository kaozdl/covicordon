from django.db import models

class Payment(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    deposited_at = models.DateField(null=True, blank=True)
    verified = models.BooleanField(default=False, blank=True)
    member = models.ForeignKey('members.Member', on_delete=models.DO_NOTHING)
    ammount = models.FloatField()
    attachment = models.FileField()
