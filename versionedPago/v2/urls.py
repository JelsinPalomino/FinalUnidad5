from rest_framework.routers import DefaultRouter
from versionedPago.v2.api import ExpiredPaymentViewUser, PaymentUsersViewUser, ServicesViewUser

route = DefaultRouter()

route.register("services", ServicesViewUser, basename = "services")
route.register("payment-users", PaymentUsersViewUser, basename = "payment-user")
route.register("expired-payment", ExpiredPaymentViewUser, basename = "expired-payment")

urlpatterns = route.urls