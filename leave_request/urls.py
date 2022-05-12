from django.urls import path, include
from leave_request.views import (
    LeaveRequestFormView,
    LeaveRequestDetailView,
    LeaveRequestListView,
    search,
    index,
    image,
    )

urlpatterns = [
    path('__reload__', include("django_browser_reload.urls")),
    path('search/', search, name="search"),
    path('image', image, name='image'),
    path('', index, name="index"),
    path('new', LeaveRequestFormView.as_view(), name='leave_request_new'),
    path('<int:pk>', LeaveRequestDetailView.as_view(), name='leave_request_detail'),
    path('list', LeaveRequestListView.as_view(), name='leave_request_list'),
]
