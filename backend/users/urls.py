from . import api
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('me/', api.me, name='me'),
    path('user/<uuid:id>/', api.user_view, name='user_view'),
    path('signup/', api.signup, name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]