from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

from app.permissions import IsOwner


class BillingViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Manage user's billing in the database.
    """
    queryset = Billing.objects.all()
    serializer_class = BillgingSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Billing.objects.filter(user=self.request.user)


class BillViewSet(viewsets.ModelViewSet):
  
    """
    Manage user's bills in the database.
    """
    
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user_billing = Billing.objects.get(user=self.request.user)
        if not user_billing:
            Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = self.queryset.filter(billing=user_billing)

        category = self.request.query_params.get('category')

        if category:
            queryset = queryset.filter(categories__name__contains=category)

        return queryset

    def perform_create(self, serializer):
        """Create a new object"""
        user_billing = Billing.objects.get(user=self.request.user)
        if not user_billing:
            Response(status=status.HTTP_400_BAD_REQUEST)
        serializer.save(billing=user_billing)
