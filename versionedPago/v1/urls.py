from rest_framework.routers import DefaultRouter
from versionedPago.v1.api import PaymentView

route = DefaultRouter()
route.register("pago", PaymentView, basename="pago")

urlpatterns = route.urls