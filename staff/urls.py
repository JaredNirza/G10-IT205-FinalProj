from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('new/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
]