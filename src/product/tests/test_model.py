from django.test import TestCase

from ..models import Product


class TestProductModel(TestCase):
    """
    Test product's model
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description',
            price=322.0,
            quantity=10,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            price=109.0,
            quantity=9,
        )

    def test_product_creation(self):
        product_1 = Product.objects.get(name='Test Product 1')
        product_2 = Product.objects.get(name='Test Product 2')
        self.assertEqual(self.product_1.name, product_1.name)
        self.assertEqual(self.product_1.description, product_1.description)
        self.assertEqual(self.product_1.price, product_1.price)
        self.assertEqual(self.product_1.quantity, product_1.quantity)
        self.assertEqual(self.product_2.name, product_2.name)
        self.assertEqual(self.product_2.description, product_2.description)
        self.assertEqual(self.product_2.price, product_2.price)
        self.assertEqual(self.product_2.quantity, product_2.quantity)
