from rest_framework import pagination
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.viewsets import ViewSetMixin

from .models import Establishment
from .serializers import (
    EstablishmentSerializer, EstablishmentCreateUpdateSerializer
)


class EstablishmentPagination(pagination.PageNumberPagination):
    """
    Pagination class for establishment listing
    """
    page_size = 5


class EstablishmentListView(ListAPIView):
    """
    Establishment listing
    """
    queryset = Establishment.objects.all().order_by('id')
    serializer_class = EstablishmentSerializer
    pagination_class = EstablishmentPagination


class EstablishmentCreateView(CreateAPIView):
    """
    Individual establishment creation view
    """
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentCreateUpdateSerializer


class EstablishmentViewSet(ViewSetMixin,
                           RetrieveAPIView,
                           UpdateAPIView,
                           DestroyAPIView):
    """
    Establishment viewset
    Retrieve, update or delete establishment
    """
    queryset = Establishment.objects.all()

    def get_serializer_class(self):
        """
        Returns the appropriate serializer
        :return:
        """
        if self.action in ('update', 'partial_update'):
            return EstablishmentCreateUpdateSerializer
        else:
            return EstablishmentSerializer
