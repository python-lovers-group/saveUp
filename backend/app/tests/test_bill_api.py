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


def create_sample_category(name, user):
    """Create category or return if it existed"""
    if Category.objects.filter(name=name, user=user).count():
        return Category.objects.get(name=name)
    else:
        return Category.objects.create(name=name, user=user)


class BillApiTestUnauthorized(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_permissions_and_auth_is_required(self):
        """Test that authentication credential is required."""
        response = self.client.get(BILL_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


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
        # self.assertEqual(response.data['list_of_bills'], serializer.data)

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
        category = create_sample_category("TestCategory", self.user)

        payload = {
            "billing": get_users_billing(self.user),
            "categories": category.name,
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

        categories = [create_sample_category(name, self.user) for name in
                      ["TestCategory1", "TestCategory2", "TestCategory3"]]

        payload = {
            "billing": get_users_billing(self.user),
            "categories": [category.name for category in categories],
            "price": 99,
            "where": "Test",
            "description": "test test"
        }
        response = self.client.post(BILL_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bill = Bill.objects.get(id=response.data.get("id"))
        serializer = BillSerializer(bill)
        self.assertEqual(response.data, serializer.data)

    def test_filter_bills_by_category(self):
        """Test filtering Bills queryset by category."""
        category1 = create_sample_category("TestCategory1", self.user)
        category2 = create_sample_category("TestCategory2", self.user)

        bill1 = create_sample_bill(user=self.user)
        bill1.categories.add(category1)
        bill1.categories.add(category2)

        bill2 = create_sample_bill(user=self.user)
        bill2.categories.add(category1)

        bill3 = create_sample_bill(user=self.user)
        bill3.categories.add(category2)

        query = {
            "category": f"{category1.name}"
        }
        response = self.client.get(BILL_URL, query)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bills = Bill.objects.filter(categories__name__contains=category1.name)
        self.assertEqual(len(response.data), len(bills))

    def test_represent_category_in_bill_as_name(self):
        """Test representing category as name in Bill"""
        category = create_sample_category("TestCategory1", self.user)

        payload = {
            "billing": get_users_billing(self.user),
            "categories": category.name,
            "price": 99,
            "where": "Test",
            "description": "test test"
        }
        response = self.client.post(BILL_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bill = Bill.objects.get(id=response.data.get("id"))
        serializer = BillSerializer(bill)
        self.assertEqual(serializer.data['categories'][0], category.name)
