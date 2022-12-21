from rest_framework.routers import DefaultRouter
from versionedPago.v2.api import ExpiredPaymentView, PaymentUsersView, ServicesView

route = DefaultRouter()
route.register("services", ServicesView, basename = "services")
route.register("payment-users", PaymentUsersView, basename = "payment-user")
route.register("expired-payment", ExpiredPaymentView, basename = "expired-payment")



urlpatterns = route.urls