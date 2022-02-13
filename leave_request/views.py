from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from leave_request.forms import LeaveRequestForm
from leave_request.models import LeaveRequest
from django.contrib import messages
from django.contrib.auth.mixins  import LoginRequiredMixin

class LeaveRequestFormView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leave_request/leave_request_form.html'
    form_class = LeaveRequestForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('leave_request_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Leave request submitted successfully')
        return super().form_valid(form)

class LeaveRequestDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('login')
    model = LeaveRequest
    template_name = 'leave_request/leave_request_detail.html'

class LeaveRequestListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    template_name = 'leave_request/leave_request_list.html'
    model = LeaveRequest

    def get_queryset(self):
        leave_requests = LeaveRequest.objects.filter(user=self.request.user)
        return leave_requests 
