from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from app.models import (
    Bill,
    Billing,
)


class BillSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializer for Bill objects"""

    categories = TagListSerializerField()

    class Meta:
        model = Bill
        exclude = ['billing']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price cannot be negative or equal to zero.")
        return value

    def validate_where(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Localization name length must be greater than 3.")
        return value


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
