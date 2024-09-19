from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # ==================== Simple JWT ====================
    path ( 'login/' , TokenObtainPairView.as_view( ) , name = 'token_obtain_pair' ) ,
    path ( 'token/refresh/' , TokenRefreshView.as_view( ) , name = 'token_refresh' ) ,
    path ( 'me/' , TokenVerifyView.as_view( ), name = 'token_verify' ) , # frontend should send request to \
    # this endpoint to verify the token every time a user reloads the page

    # ========== Password urls ==========
    path( 'forgot-password/', ForgotPasswordAPIView.as_view(), name = 'forgot_password' ),
    path( 'forgot-password/<int:user_id>/<str:token>/', PasswordResetConfirmAPIView.as_view(),
                name = "password-reset-confirm" ),

    # ========== Register urls ==========
    path( 'register/', RegisterAPIView.as_view(), name = 'register'),
    path( 'register/send-code/', VerifyCodeAPIView.as_view(), name = 'verify_code'),
    path( 'register/verify-code/',  VerifyCodeAPIView.as_view(), name = 'verify_code'),

]

