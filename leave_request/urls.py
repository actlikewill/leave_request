from django.urls import path
from leave_request.views import (
    LeaveRequestFormView,
    LeaveRequestDetailView,
    LeaveRequestListView,
    )

urlpatterns = [
    path('new', LeaveRequestFormView.as_view(), name='leave_request_new'),
    path('<int:pk>', LeaveRequestDetailView.as_view(), name='leave_request_detail'),
    path('', LeaveRequestListView.as_view(), name='leave_request_list'),
]
