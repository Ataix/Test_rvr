from unittest import TestCase

from ..models import Establishment


class TestEstablishmentModel(TestCase):
    """
    Test the establishment model
    """
    def setUp(self):
        self.est_1 = Establishment.objects.create(
            name='Establishment 1',
            description='Establishment 1',
            locations='Establishment locations 1',
            opening_hours='7-24',
        )

    def test_establishment_creation(self):
        est_1 = Establishment.objects.get(name='Establishment 1')
        self.assertEqual(self.est_1.name, est_1.name)
        self.assertEqual(self.est_1.description, est_1.description)
        self.assertEqual(self.est_1.locations, est_1.locations)
        self.assertEqual(self.est_1.opening_hours, est_1.opening_hours)
