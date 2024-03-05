import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Establishment
from ..serializers import EstablishmentSerializer


client = APIClient()


class TestListView(TestCase):
    """
    Test the list view
    """
    def setUp(self):
        Establishment.objects.create(
            name='Establishment 1',
            description='Establishment 1',
            locations='Establishment locations 1',
            opening_hours='7-24',
        )
        Establishment.objects.create(
            name='Establishment 2',
            description='Establishment 2',
            locations='Establishment locations 2',
            opening_hours='7-24',
        )
        Establishment.objects.create(
            name='Establishment 3',
            description='Establishment 3',
            locations='Establishment locations 3',
            opening_hours='7-24',
        )
        Establishment.objects.create(
            name='Establishment 4',
            description='Establishment 4',
            locations='Establishment locations 4',
            opening_hours='7-24',
        )

    def test_list_view(self):
        response = client.get('/api/v1/establishment/list/')
        products = Establishment.objects.all().order_by('id')
        serializer = EstablishmentSerializer(products, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDetailView(TestCase):
    """
    Test the detail view
    """
    def setUp(self):
        self.est_1 = Establishment.objects.create(
            name='Establishment 1',
            description='Establishment 1',
            locations='Establishment locations 1',
            opening_hours='7-24',
        )

    def test_valid_detail_view(self):
        response = client.get(f'/api/v1/establishment/{self.est_1.pk}/')
        product = Establishment.objects.get(pk=self.est_1.pk)
        serializer = EstablishmentSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_detail_view(self):
        response = client.get(f'/api/v1/product/{30}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestCreateView(TestCase):
    """
    Test the create view
    """
    def setUp(self):
        self.valid_payload = {
            'name': 'Test Establishment 1',
            'description': 'Test Establishment 1',
            'locations': 'Establishment locations 1',
            'opening_hours': '7-24',
        }
        self.invalid_payload = {
            'name': '',
            'description': '',
            'locations': 'Establishment locations 1',
            'opening_hours': '7-24',
        }

    def test_valid_create_view(self):
        response = self.client.post(
            f'/api/v1/establishment/create/',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_view(self):
        response = self.client.post(
            f'/api/v1/establishment/create/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateView(TestCase):
    """
    Test for update view (put, patch)
    """
    def setUp(self):
        self.est_1 = Establishment.objects.create(
            name='Establishment 1',
            description='Establishment 1',
            locations='Establishment locations 1',
            opening_hours='7-24',
        )
        self.est_2 = Establishment.objects.create(
            name='Establishment 2',
            description='Establishment 2',
            locations='Establishment locations 2',
            opening_hours='7-24',
        )
        self.valid_payload_put = {
            'name': 'Edited Est',
            'description': 'Edited Est',
            'locations': 'Edited locations',
            'opening_hours': '9-21',
        }
        self.invalid_payload_put = {
            'name': '',
            'description': '',
            'locations': 'Edited locations',
            'opening_hours': '9-21',
        }
        self.valid_payload_patch = {
            'locations': 'Edited locations 1',
            'opening_hours': '9-21'
        }
        self.invalid_payload_patch = {
            'locations': '',
            'opening_hours': ''
        }

    def test_valid_put(self):
        response = self.client.put(
            f'/api/v1/establishment/{self.est_1.pk}/',
            data=json.dumps(self.valid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_put(self):
        response = self.client.put(
            f'/api/v1/establishment/{self.est_1.pk}/',
            data=json.dumps(self.invalid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_patch(self):
        response = self.client.patch(
            f'/api/v1/establishment/{self.est_2.pk}/',
            data=json.dumps(self.valid_payload_patch),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_patch(self):
        response = self.client.patch(
            f'/api/v1/establishment/{self.est_2.pk}/',
            data=json.dumps(self.invalid_payload_patch),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestDeleteView(TestCase):
    """
    Tests for delete view
    """
    def setUp(self):
        self.est_1 = Establishment.objects.create(
            name='Establishment 1',
            description='Establishment 1',
            locations='Establishment locations 1',
            opening_hours='7-24',
        )

    def test_valid_delete(self):
        response = self.client.delete(f'/api/v1/establishment/{self.est_1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = self.client.delete(f'/api/v1/establishment/{30}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
