from django.urls import path, include

from rest_framework.routers import DefaultRouter
from app.views import BillingViewSet


router = DefaultRouter()
router.register(r"billing", BillingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]