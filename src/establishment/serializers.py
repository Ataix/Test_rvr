from rest_framework import serializers

from .models import Establishment
from .utils import locations_clearance, opening_hours_clearance


class EstablishmentSerializer(serializers.ModelSerializer):
    """
    Establishment's serializer
    """
    class Meta:
        model = Establishment
        fields = (
            'id',
            'name',
            'description',
            'locations',
            'opening_hours',
        )


class EstablishmentCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Establishment's serializer for create and update operations
    """
    class Meta:
        model = Establishment
        fields = (
            'id',
            'name',
            'description',
            'locations',
            'opening_hours',
        )

    def create(self, validated_data):
        """
        Override establishment create method.
        Modify locations, check opening hours for correctness
        :param validated_data:
        :return: establishment object
        """
        validated_data['locations'] = locations_clearance(
            validated_data['locations']
        )

        opening_hours_clearance(validated_data['opening_hours'])

        establishment = Establishment.objects.create(**validated_data)
        return establishment

    def update(self, instance, validated_data):
        """
        Override establishment update method.
        Modify locations, check opening hours for correctness
        :param instance:
        :param validated_data:
        :return: instance object
        """
        if 'locations' in validated_data:
            validated_data['locations'] = locations_clearance(
                validated_data['locations']
            )

        if 'opening_hours' in validated_data:
            opening_hours_clearance(validated_data['opening_hours'])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
