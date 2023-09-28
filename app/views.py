from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,BasePermission,IsAuthenticated
from rest_framework.decorators import permission_classes



class CustomUserPermission1(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.method == 'PUT':
            return True
        elif request.method == 'DELETE':
            return True
        return request.user and request.user.IsAdminUser

class ViagemView():
    permission_classes = [CustomUserPermission1]
    
    def get(self, request):
        serializer = ViagensSerializer(Viagens.objects.all(), many=True)
        return Response(status=200, data=serializer.data)
    
    def post(self, request):
        serializer = ViagensSerializer(data=request.data)
        if serializer.is_valid():
            viagens = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,data = serializer.errors)
    
    def put(self, request, viagemId = ''):
        viagensFound = ViagensSerializer.objects.get(id=viagemId)
        viagensJson = request.data 
        viagensSerialized = ViagensSerializer(viagensFound, data=viagensJson)
        if viagensSerialized.is_valid():
            viagensSerialized.save()
            return Response(status=status.HTTP_200_OK, data=viagensSerialized.data)
        return Response(status= status.HTTP_400_BAD_REQUEST, data = serializers.errors)
    
    def delete(self, request, viagemId = ''):
        viagensFound = ViagensSerializer.objects.get(id=viagemId)
        try:
            viagensFound.delete()
            return Response(status=status.HTTP_200_OK,data="Usuario deletado")
        except:
            return Response(status=status.HTTP_204_NO_CONTENT,data=serializers.errors)

class CategoriasView(models.Model):
    
    def get(self, request):
        serializer = CategoriasSerializer(Categorias.objects.all(), many=True)
        return Response(status=200, data=serializer.data)
    
    def post(self, request):
        serializers = CategoriasSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializers.errors)
    
    def delete(self, request,categoriaId = ''):
        categoriaFound = CategoriasSerializer.get(categoriaId=categoriaId)
        try:
            categoriaFound.delete()
            return Response(data="Usuario apagado",status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializers.erro)
        
    def put(self, request,categoriaId = ''):
        categoriaFound = CategoriasSerializer.get(categoriaId=categoriaId)
        categoriaSerialized = CategoriasSerializer.get(categoriaFound,data=request.data)
        if categoriaSerialized.is_valid():
            categoriaSerialized.save()
            return Response(data="Usuario atualizado",status=status.HTTP_200_OK)
        return Response(data="Usuario atualizado",status=status.HTTP_400_BAD_REQUEST,data=categoriaSerialized.errros)


class ReservaView(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializers
    permission_classes = (IsAuthenticated,)
    
class PagamentosView(viewsets.ModelViewSet):
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializers
    permission_classes = (IsAuthenticated,)
    

class FotosView(viewsets.ModelViewSet):
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializers
    permission_classes = (IsAuthenticated,)
    
class Auxiliar(viewsets.ModelViewSet):
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializers
    permission_classes = (IsAdminUser,)