from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


options = (
    (1, "Pendente"),
    (2, "Aprovado"),
    (3, "Recusado"),
)


class Fotos():
    link = models.CharField(max_length=2000,  blank=False, null=False),

class Categorias(models.Model):
    categoria = models.CharField(max_length=200, blank=False,null=False),

class Viagens(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=False),
    descricao = models.CharField(max_length=2000,blank=False, null=False),
    endereco = models.CharField(max_length=200, blank=False, null=False),
    cidade = models.CharField(max_length=200, blank=False,null=False),
    dataInicial = models.DateTimeField(default=timezone.now,blank=False,null=False),
    dataFinal = models.DateTimeField(default=timezone.now,blank=False,null=False),
    fotos = models.ForeignKey(Fotos, null=False, blank=False)
    valorDiaria = models.DecimalField(blank=False,null=False,nullable=False,decimal_places=2)
    categoria = models.ForeignKey(Categoria, null=False, blank=False)

class Pagamentos(models.Model):
    usuario = models.ForeignKeyField(User,blank=False,null=False)
    numeroCartao = models.CharField(max_length=20)
    numeroBoleto = models.CharField(max_length=2000)
    codigoPix = models.CharField(max_length=2000)
    status = models.IntegerField(choices=options,default=1)
    
class Reserva(models.Model):
    usuario = models.ForeignKey(User, blank=False, null=False,related_name="usurioReserva")
    viagem = models.ForeignKey(Viagens,blank=False,null=False,related_name="viagemReseva")
    dataReserva = models.DateTimeField(),
    valorDiaria = models.ForeignKey(Viagens, blank=False, null=False,related_name="diariaViagem")
    dias = models.IntegerField(blank=False, null=False),
    valorFinal = models.DecimalField(null=False,blank=False,decimal_places=2)
    animal = models.BooleanField(default=False)
    nota = models.DecimalField(null=False, blank=False,max_digits=2,decimal_places=1,validators=[MinValueValidator(0),MaxValueValidator(10)])
    pagamentoId = models.ForeignKey(Pagamento, blank=False, related_name="pagamentoId")
    