from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/', include('questions.urls')),  # API routes
    path('admin/', admin.site.urls),         # Admin panel
    path('', TemplateView.as_view(template_name="index.html")),  # Serve Vue frontend
]
