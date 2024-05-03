from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import views as jwt_views
from .views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("register/", csrf_exempt(RegisterAPIView.as_view()), name="register"),
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
