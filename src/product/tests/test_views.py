import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Product
from ..serializers import ProductSerializer


client = APIClient()


class TestListView(TestCase):
    """
    Test product's list view
    """
    def setUp(self):
        Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            price=100.0,
            quantity=10,
        )
        Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            price=1088.0,
            quantity=1,
        )
        Product.objects.create(
            name='Test Product 3',
            description='Test Description 3',
            price=9902.0,
            quantity=13,
        )
        Product.objects.create(
            name='Test Product 4',
            description='Test Description 4',
            price=8869.0,
            quantity=199,
        )

    def test_list_view(self):
        response = client.get('/api/v1/product/list/')
        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDetailView(TestCase):
    """
    Test product's detail view
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            price=10340.7,
            quantity=1,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            price=1243.3,
            quantity=31,
        )
        self.product_3 = Product.objects.create(
            name='Test Product 3',
            description='Test Description 3',
            price=9902.4,
            quantity=95,
        )

    def test_valid_detail_view(self):
        response = client.get(f'/api/v1/product/{self.product_2.pk}/')
        product = Product.objects.get(pk=self.product_2.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_detail_view(self):
        response = client.get(f'/api/v1/product/{30}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestCreateView(TestCase):
    """
    Test product's create view
    """
    def setUp(self):
        self.valid_payload = {
            'name': 'Test Product 1',
            'description': 'Test Description 1',
            'price': 10340.7,
            'quantity': 13,
        }
        self.invalid_payload = {
            'name': '',
            'description': '',
            'price': 1243.3,
            'quantity': 31,
        }

    def test_valid_create_view(self):
        response = self.client.post(
            f'/api/v1/product/create/',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_view(self):
        response = self.client.post(
            f'/api/v1/product/create/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateView(TestCase):
    """
    Test product's update view (put, patch)
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            price=10340.7,
            quantity=1,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            price=1243.3,
            quantity=31,
        )
        self.valid_payload_put = {
            'name': 'Edited Product',
            'description': 'Edited Descr',
            'price': 10.8,
            'quantity': 1,
        }
        self.invalid_payload_put = {
            'name': '',
            'description': '',
            'price': -1,
            'quantity': -1,
        }
        self.valid_payload_patch = {
            'price': 10.8,
            'quantity': 1,
        }
        self.invalid_payload_patch = {
            'price': '',
            'quantity': '',
        }

    def test_valid_put(self):
        response = self.client.put(
            f'/api/v1/product/{self.product_1.pk}/',
            data=json.dumps(self.valid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_put(self):
        response = self.client.put(
            f'/api/v1/product/{self.product_1.pk}/',
            data=json.dumps(self.invalid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_patch(self):
        response = self.client.patch(
            f'/api/v1/product/{self.product_2.pk}/',
            data=json.dumps(self.valid_payload_patch),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_patch(self):
        response = self.client.patch(
            f'/api/v1/product/{self.product_2.pk}/',
            data=json.dumps(self.invalid_payload_patch),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestDeleteView(TestCase):
    """
    Test product's delete view
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            price=10340.7,
            quantity=1,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            price=1243.3,
            quantity=31,
        )

    def test_valid_delete(self):
        response = self.client.delete(f'/api/v1/product/{self.product_1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = self.client.delete(f'/api/v1/product/{0}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
