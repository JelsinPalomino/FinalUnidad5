from django.db import models
from users.models import User


class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    logo = models.CharField(max_length=300)

    class Meta:
        db_table = "services"   
   
    def __str__(self):
        return self.name

class PaymentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount =  models.IntegerField()
    payment_date =  models.DateField(auto_now_add=True)
    expiration_date =  models.DateField()

    class Meta:
        db_table = "payment_user"
    
    def __str__(self):
        return str(self.pk)
    

class ExpiredPayments(models.Model):
    payment_user_id = models.ForeignKey(PaymentUser, on_delete = models.CASCADE)
    penalty_free_amount = models.IntegerField()

    class Meta:
        db_table = "expired_payments"


