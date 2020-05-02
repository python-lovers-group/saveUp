from django.urls import path, include

from rest_framework.routers import DefaultRouter
from app.views import BillingViewSet, BillViewSet


router = DefaultRouter()
router.register(r"billing", BillingViewSet)
router.register(r"bills", BillViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
