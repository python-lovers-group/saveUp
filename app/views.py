from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from app.models import (
    Bill,
    Billing,
    Category,
)
from app.serializers import (
    BillgingSerializer,
    # CategorySerializer,
    BillSerializer
)


class BillingViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillgingSerializer

    authentication_classes = []
    permission_classes = []


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    authentication_classes = []
    permission_classes = []
