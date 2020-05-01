from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from app.models import (
    Bill,
    Billing,
    Category,
)
from app.serializers import (
    BillgingSerializer,
    BillSerializer
    # CategorySerializer
)


class BillingViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Manage user's billing in the dabase.
    """
    queryset = Billing.objects.all()
    serializer_class = BillgingSerializer

    authentication_classes = []
    permission_classes = []


class BillViewSet(viewsets.ModelViewSet):
  
    """
    Manage user's bills in the database.
    """
    
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')

        if category:
            queryset = queryset.filter(categories__name__contains=category)

        return queryset
