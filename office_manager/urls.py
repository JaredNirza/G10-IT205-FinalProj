from django.contrib import admin
from django.urls import path, include
from .views import home, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('inventory/', include('inventory.urls')),
    path('staff/', include('staff.urls')),
    path('requests/', include('requests.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]