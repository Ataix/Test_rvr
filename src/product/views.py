from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView,
    UpdateAPIView
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSetMixin

from .models import Product
from .serializers import ProductSerializer, ProductCreateUpdateSerializer


class ProductPagination(PageNumberPagination):
    """
    Pagination customization for product
    """
    page_size = 5


class ProductListView(ListAPIView):
    """
    Product listing view
    """
    paginator_class = ProductPagination
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    """
    Individual view for product creating
    """
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductViewSet(ViewSetMixin,
                     RetrieveAPIView,
                     UpdateAPIView,
                     DestroyAPIView):
    """
    Product viewset
    Retrieve, update and delete a product
    """
    queryset = Product.objects.all()

    def get_serializer_class(self):
        """
        Returns the appropriate serializer
        :return:
        """
        if self.action in ('update', 'partial_update'):
            return ProductCreateUpdateSerializer
        else:
            return ProductSerializer
