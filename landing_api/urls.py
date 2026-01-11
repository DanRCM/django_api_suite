# landing_api/urls.py
from django.urls import path
from .views import LandingAPI

app_name = 'landing_api'

urlpatterns = [
    # La ruta se convierte en: /landing/api/index/
    path('index/', LandingAPI.as_view(), name='index'),
]