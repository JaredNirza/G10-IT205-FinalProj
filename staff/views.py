from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q 
from .models import Employee
from .forms import EmployeeForm

# READ: List all employees with Search Functionality
class EmployeeListView(ListView):
    model = Employee
    template_name = 'staff/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Employee.objects.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) | 
                Q(department__icontains=query) |
                Q(email__icontains=query)
            )
        return Employee.objects.all()

# READ: View a single employee's details
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'staff/employee_detail.html'

# CREATE: Add a new employee
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'staff/employee_form.html'
    success_url = reverse_lazy('employee-list')

# UPDATE: Edit an existing employee
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'staff/employee_form.html'
    success_url = reverse_lazy('employee-list')

# DELETE: Remove an employee
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'staff/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')