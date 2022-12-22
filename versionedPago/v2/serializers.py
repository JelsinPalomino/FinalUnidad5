from versionedPago.models import *
from rest_framework.serializers import ModelSerializer

class ServicesSerializers(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class PaymentUsersSerializers(ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = "__all__"

class ExpiredPaymentsSerializers(ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = "__all__"
