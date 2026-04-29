from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('add/', ItemCreateView.as_view(), name='item-add'), 
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]