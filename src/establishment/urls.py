from django.urls import path

from .views import (
    EstablishmentListView, EstablishmentCreateView, EstablishmentViewSet
)

urlpatterns = [
    path('list/', EstablishmentListView.as_view()),
    path('create/', EstablishmentCreateView.as_view()),
    path('<int:pk>/', EstablishmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]
