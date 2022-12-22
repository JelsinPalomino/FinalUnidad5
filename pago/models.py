from django.db import models
from users.models import User

class Payment(models.Model):
    SERVICES = (
        ("Netflix","Netflix"),
        ("Amazon Video","Amazon Video"),
        ("Star +","Star +"),
        ("Paramount +","Paramount +"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    services = models.CharField(max_length=100, choices = SERVICES)
    pay_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "pagos"