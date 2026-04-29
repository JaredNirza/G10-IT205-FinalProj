from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from inventory.models import Item
from staff.models import Employee
from requests.models import SupplyRequest

def home(request):
    if request.user.is_authenticated:
        context = {
            'item_count': Item.objects.count(),
            'employee_count': Employee.objects.count(),
            'request_count': SupplyRequest.objects.filter(status='Pending').count(),
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'landing.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        Employee.objects.create(
            user=self.object,
            first_name=self.object.username,
            email=f"{self.object.username}@supplysync.com"
        )
        return response