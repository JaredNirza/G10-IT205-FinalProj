from django.urls import path
from .views import (
    SupplyRequestListView, 
    SupplyRequestDetailView, 
    SupplyRequestCreateView, 
    SupplyRequestUpdateView, 
    SupplyRequestDeleteView
)

urlpatterns = [
    path('', SupplyRequestListView.as_view(), name='request-list'),
    path('<int:pk>/', SupplyRequestDetailView.as_view(), name='request-detail'),
    path('add/', SupplyRequestCreateView.as_view(), name='request-create'),
    path('<int:pk>/edit/', SupplyRequestUpdateView.as_view(), name='request-update'),
    path('<int:pk>/delete/', SupplyRequestDeleteView.as_view(), name='request-delete'),
]