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
    categories = CategorySerializer(many=True)

    class Meta:
        model = Bill
        exclude = ['billing']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price cannot be negative or equal to zero.")
        return value

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        bill = Bill.objects.create(**validated_data)
        for category_data in categories_data:
            Category.objects.create(bill=bill, **category_data)
        return bill


class BillingSerializer(serializers.ModelSerializer):
    """Serializer for Billing objects + extra field bills which is related to BillSerializer"""

    bills = BillSerializer(many=True, read_only=True)
    total_bills = serializers.SerializerMethodField()

    class Meta:
        model = Billing
        fields = '__all__'
        read_only_fields = ['user']

    def get_total_bills(self, obj):
        total = 0
        for bill in Bill.objects.filter(billing=obj):
            total += bill.price
        return total
