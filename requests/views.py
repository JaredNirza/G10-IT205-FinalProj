from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SupplyRequest

# READ
class SupplyRequestListView(ListView):
    model = SupplyRequest
    template_name = 'requests/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        queryset = SupplyRequest.objects.all()     
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset

# READ
class SupplyRequestDetailView(DetailView):
    model = SupplyRequest
    template_name = 'requests/request_detail.html'

# CREATE
class SupplyRequestCreateView(CreateView):
    model = SupplyRequest
    fields = ['employee', 'item', 'quantity_requested', 'status']
    template_name = 'requests/request_form.html'
    success_url = reverse_lazy('request-list')

# UPDATE
class SupplyRequestUpdateView(UpdateView):
    model = SupplyRequest
    fields = ['employee', 'item', 'quantity_requested', 'status']
    template_name = 'requests/request_form.html'
    success_url = reverse_lazy('request-list')

# DELETE
class SupplyRequestDeleteView(DeleteView):
    model = SupplyRequest
    template_name = 'requests/request_confirm_delete.html'
    success_url = reverse_lazy('request-list')