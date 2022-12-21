from versionedPago.v2.serializers import ExpiredPaymentsSerializers, PaymentUsersSerializers, ServicesSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from versionedPago.models import Services, ExpiredPayments, PaymentUser
from versionedPago.v2.pagination import SimplePagination

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny

class ServicesView(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    http_method_names = ['get']

    permission_classes = [IsAuthenticated]
    throttle_scope = 'services'

class PaymentUsersView(ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUsersSerializers
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'expiration_date']

    permission_classes = [IsAuthenticated]

    throttle_scope = 'pagos'
    
class ExpiredPaymentView(ModelViewSet):
    queryset = ExpiredPayments.objects.all()
    serializer_class = ExpiredPaymentsSerializers
    pagination_class = SimplePagination
    http_method_names = ['get','post']
    permission_classes = [IsAuthenticated]
    throttle_scope = 'expired'
    