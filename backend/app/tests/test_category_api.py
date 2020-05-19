from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from app.models import Category, Bill, Billing
from app.serializers import CategorySerializer, BillSerializer

CATEGORY_URL = "/api/categories/"
SELECT_CATEGORY_URL = CATEGORY_URL + "select_category/"


def get_detail_url(category):
    """Return detail url for bill."""
    return CATEGORY_URL + str(category.id) + "/"


def get_users_billing(user):
    """Return User's billing."""
    return Billing.objects.get(user=user)


def create_sample_category(name, user):
    """Create category or return if it existed"""
    if Category.objects.filter(name=name, user=user).count():
        return Category.objects.get(name=name)
    else:
        return Category.objects.create(name=name, user=user)


def create_sample_bill(user, category_name=0, price=10, where='SampleLocalization'):
    """Create and return sample Bill."""

    bill = Bill.objects.create(billing=get_users_billing(user),
                               price=price,
                               where=where)

    if category_name:
        category_name = Category.objects.get(user=user, name=category_name)
        bill.categories.add(category_name)

    return bill


class CategoryApiTestUnauthorized(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_permissions_and_auth_is_required(self):
        """Test that authentication credential is required."""
        response = self.client.get(CATEGORY_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CategoryApiTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='test123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_categories_list(self):
        """Test retrieving list of user's Categories."""
        create_sample_category("TestCategory1", self.user)
        create_sample_category("TestCategory2", self.user)

        response = self.client.get(CATEGORY_URL)

        categories = Category.objects.filter(user=self.user)
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_category_detail_view(self):
        """Test detail view of user's Category."""
        category = create_sample_category("TestCategory", self.user)

        url = get_detail_url(category)
        response = self.client.get(url)
        serializer = CategorySerializer(category)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_category(self):
        """Test creating new Category object."""

        payload = {
            "name": "TestCategory",
            "user": self.user
        }

        response = self.client.post(CATEGORY_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        category = Category.objects.get(id=response.data.get("id"))
        serializer = CategorySerializer(category)
        self.assertEqual(response.data, serializer.data)

    def test_select_category(self):
        """Test selecting category and returning bills with this one"""

        category1 = create_sample_category("TestCategoryA", self.user)
        category2 = create_sample_category("TestCategoryB", self.user)

        response = self.client.get(CATEGORY_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bill1 = create_sample_bill(self.user, category_name=category1.name)
        bill2 = create_sample_bill(self.user, category_name=category1.name)
        bill3 = create_sample_bill(self.user, category_name=category2.name)

        serializers_dicts = [BillSerializer(bill).data for bill in [bill1, bill2, bill3]]

        payload = {"category": category1.name}
        response = self.client.get(SELECT_CATEGORY_URL, payload)
        self.assertEqual(len(response.data), len(
            [serializer for serializer in serializers_dicts if category1.name in serializer['categories']]))
