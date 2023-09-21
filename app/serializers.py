from rest_framework import serializers
from models import *

class UserSerializer(serializers.Model):
    class Meta:
        model = User
        fields = '__all__'

class FotoSerializer(serializers.Model):
    class Meta:
        model = Fotos
        fields = '__all__'


class CategoriasSerializer(serializers.Model):
    class Meta:
        model = Categorias
        fields = '__all__'

class ViagensSerializer(serializers.Model):
    class Meta:
        model = Viagens
        fields = '__all__'
        
class PagamentosSerializers(serializers.Model):
    class Meta:
        models = Pagamentos
        filter_fields = '__all__'

class ReservaSerializers(serializers.Model):
    class Meta:
        models = Reserva
        filter_fields = '__all__'