from versionedPago.v1.serializers import PaymentSerializer
from pago.models import Payment
from versionedPago.v1.pagination import SimplePagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.throttling import UserRateThrottle
from rest_framework import filters

class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    pagination_class = SimplePagination
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__id', 'fecha_pago', 'servicio']

    throttle_scope = 'get'

    # Class UserRate
    #throttle_classes = [UserRateThrottle]