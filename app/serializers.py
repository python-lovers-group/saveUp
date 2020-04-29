from rest_framework import serializers
from app.models import (
    Bill,
    Billing,
    Category,
)


class BillgingSerializer(serializers.ModelSerializer):
    """Serializer for Billing objects"""

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Billing
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category objects"""

    name = serializers.CharField(max_length=255)

    class Meta:
        model = Category
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    """Serializer for Bill objects"""

    billing = serializers.StringRelatedField(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = '__all__'
