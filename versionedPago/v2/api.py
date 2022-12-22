from versionedPago.v2.serializers import ExpiredPaymentsSerializers, PaymentUsersSerializers, ServicesSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from versionedPago.models import Services, ExpiredPayments, PaymentUser
from versionedPago.v2.pagination import SimplePagination

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
#from django.shortcuts import get_object_or_404

# TODO: Services User
class ServicesViewUser(ModelViewSet):
    queryset = Services.objects.all()

    throttle_scope = 'services'

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy' or self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAdminUser]
        return [permissions() for permissions in permission_classes]
    def get_serializer_class(self):
        return ServicesSerializers


# TODO: Payment Users
class PaymentUsersViewUser(ModelViewSet):
    queryset = PaymentUser.objects.all()
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'expiration_date']
    
    throttle_scope = 'pagos'

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permissions() for permissions in permission_classes]

    def get_serializer_class(self):
        return PaymentUsersSerializers


# TODO: Expired Payment
class ExpiredPaymentViewUser(ModelViewSet):
    queryset = ExpiredPayments.objects.all()
    pagination_class = SimplePagination

    throttle_scope = 'expired'

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy' or self.action == 'retrieve':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return ExpiredPaymentsSerializers
