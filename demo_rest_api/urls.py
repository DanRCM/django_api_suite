from django.urls import path
from . import views

urlpatterns = [
   # Ruta para GET (lista) y POST (crear)
   path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources"),
   
   # Ruta para PUT, PATCH, DELETE (necesita el ID)
   path("<str:id>/", views.DemoRestApiItem.as_view(), name="demo_rest_api_item_resources"),
]