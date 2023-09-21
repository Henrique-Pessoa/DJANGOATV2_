from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class ViagemView():
    def get(self, request):
        serializer = ViagensSerializer(Viagens.objects.all(), many=True)
        return Response(status=200, data=serializer.data)
    