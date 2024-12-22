from . import api
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('me/', api.me, name='me'),
    path('user/<uuid:id>/', api.user_view, name='user_view'),
    path('signup/', api.signup, name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]