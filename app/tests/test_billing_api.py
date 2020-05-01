from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from app.models import Billing
from app.serializers import BillingSerializer


BILLING_URL = "/api/billing/"


class BillingApiTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='test123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_billing_list(self):
        """Test retrieving one-piece Billing array."""
        response = self.client.get(BILLING_URL)

        billings = Billing.objects.filter(user=self.user)
        serializer = BillingSerializer(billings, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
