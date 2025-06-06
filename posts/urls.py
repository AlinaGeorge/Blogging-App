from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view()),  # ✅
    path('api-token-auth/', obtain_auth_token),  # for login
]
