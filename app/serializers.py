from rest_framework import serializers
from app.models import (
    Bill,
    Billing,
    Category,
)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category objects"""

    name = serializers.ChoiceField(choices=Category.CATEGORY_CHOICES, default='others')

    class Meta:
        model = Category
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    """Serializer for Bill objects"""
    # billing = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Bill
        exclude = ['billing']


class BillgingSerializer(serializers.ModelSerializer):
    """Serializer for Billing objects + extra field bills which is related to BillSerializer"""

    bills = BillSerializer(many=True, read_only=True)

    class Meta:
        model = Billing
        fields = '__all__'
        read_only_fields = ['user']

