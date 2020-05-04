from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from app.models import Billing, Bill, Category
from app.serializers import BillSerializer

BILL_URL = "/api/bills/"


def get_detail_url(bill):
    """Return detail url for bill."""
    return "/api/bills/" + str(bill.id) + "/"


def get_users_billing(user):
    """Return User's billing."""
    return Billing.objects.get(user=user)


def create_sample_bill(user, price=10, where='Sample Localization'):
    """Create and return sample Bill."""
    return Bill.objects.create(billing=get_users_billing(user),
                               price=price,
                               where=where)


def create_sample_category(name):
    """Create category or return if it existed"""
    if Category.objects.filter(name=name).count():
        return Category.objects.get(name=name)
    else:
        return Category.objects.create(name=name)


class BillApiTestUnauthorized(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_permissions_and_auth_is_required(self):
        """Test that authentication credential is required."""
        response = self.client.get(BILL_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BillApiTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='test123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_bills_list(self):
        """Test retrieving list of user's Bills."""
        create_sample_bill(self.user)
        create_sample_bill(self.user)

        response = self.client.get(BILL_URL)

        bills = Bill.objects.filter(billing=get_users_billing(self.user))
        serializer = BillSerializer(bills, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['list_of_bills'], serializer.data)

    def test_bill_detail_view(self):
        """Test detail view of user's Bill."""
        bill = create_sample_bill(self.user)

        url = get_detail_url(bill)
        response = self.client.get(url)
        serializer = BillSerializer(bill)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_bill(self):
        """Test creating new Bill object."""
        category = create_sample_category("test-category")

        payload = {
            "billing": get_users_billing(self.user),
            "categories": category.id,
            "price": 99,
            "where": "Test",
            "description": "test test"
        }
        response = self.client.post(BILL_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bill = Bill.objects.get(id=response.data.get("id"))
        serializer = BillSerializer(bill)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(bill.categories.first(), category)

    def test_create_bill_with_many_categories(self):
        """Test creating new Bill object with many categories."""

        categories = [create_sample_category(name) for name in ["test-category1", "test-category2", "test-category3"]]

        payload = {
            "billing": get_users_billing(self.user),
            "categories": [category.id for category in categories],
            "price": 99,
            "where": "Test",
            "description": "test test"
        }
        response = self.client.post(BILL_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bill = Bill.objects.get(id=response.data.get("id"))
        serializer = BillSerializer(bill)
        self.assertEqual(response.data, serializer.data)
