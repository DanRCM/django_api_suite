# landing_api/views.py
from django.shortcuts import render
# 1. Importaciones de DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 2. Importaciones de Firebase Admin SDK y Python
from firebase_admin import db
import datetime

class LandingAPI(APIView):
    # 3. Atributos solicitados
    name = "Landing API"
    
    # Nombre de la colección (nodo) en Realtime Database.
    # Nota: Si tu colección en Firebase se llama diferente, cambia 'data' por ese nombre.
    collection_name = 'data' 

    def get(self, request):
        # Este método sirve para verificar que la ruta funciona
        return Response(
            {"message": "La API de Landing está funcionando correctamente"}, 
            status=status.HTTP_200_OK
        )