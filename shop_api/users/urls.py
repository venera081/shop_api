from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view()),
    path('confirm/', views.ConfirmUserAPIView.as_view()),
    path('authorization/', views.AuthorizationAPIView.as_view()),

    
    path('jwt/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


