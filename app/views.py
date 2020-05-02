from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import datetime

from app.models import (
    Bill,
    Billing,
)
from app.serializers import (
    BillingSerializer,
    BillSerializer
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
    serializer_class = BillingSerializer

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

        where = self.request.query_params.get('where')
        if where:
            queryset = queryset.filter(where=where)

        date_str = self.request.query_params.get('date')
        if date_str:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            queryset = self.queryset.filter(created_at__year=date.year,
                                            created_at__month=date.month,
                                            created_at__day=date.day)

        year_str = self.request.query_params.get('year')
        if year_str:
            year = datetime.datetime.strptime(year_str, "%Y").year
            queryset = self.queryset.filter(created_at__year=year)

        month_str = self.request.query_params.get('month')
        if month_str:
            month = datetime.datetime.strptime(month_str, "%m").month
            queryset = self.queryset.filter(created_at__month=month)

        day_str = self.request.query_params.get('day')
        if day_str:
            day = datetime.datetime.strptime(day_str, "%d").day
            queryset = self.queryset.filter(created_at__day=day)

        return queryset

    def perform_create(self, serializer):
        """Create a new object"""
        user_billing = Billing.objects.get(user=self.request.user)
        if not user_billing:
            Response(status=status.HTTP_400_BAD_REQUEST)
        serializer.save(billing=user_billing)
