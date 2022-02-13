from django.urls import path, include
from user.views import UserRegistrationView

urlpatterns = [
  path('', include('django.contrib.auth.urls')),
  path('register', UserRegistrationView.as_view(), name='user_register'),
]
