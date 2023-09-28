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


class Fotos(models.Model):
    link = models.CharField(max_length=2000,  blank=False, null=False,default="")

    def __str__(self):
        return self.link

class Categorias(models.Model):
    categoria = models.CharField(max_length=200, blank=False,null=False),

    def __str__(self):
        return self.categoria

class Viagens(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=False),
    descricao = models.CharField(max_length=2000,blank=False, null=False, ),
    endereco = models.CharField(max_length=200, blank=False, null=False,),
    cidade = models.CharField(max_length=200, blank=False,null=False,),
    dataInicial = models.DateTimeField(default=timezone.now,blank=False,null=False),
    dataFinal = models.DateTimeField(default=timezone.now,blank=False,null=False),
    fotos = models.ForeignKey(Fotos, null=False, blank=False, on_delete=models.CASCADE)
    valorDiaria = models.DecimalField(blank=False,null=False,decimal_places=2,max_digits=4)
    categoria = models.ForeignKey(Categorias, null=False, blank=False, related_name='categorasdjawdç', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pagamentos(models.Model):
    numeroCartao = models.CharField(max_length=20)
    numeroBoleto = models.CharField(max_length=2000)
    codigoPix = models.CharField(max_length=2000)
    status = models.IntegerField(choices=options,default=1)
    
    def __str__(self):
        return self.status
    
class Reserva(models.Model):
    usuario = models.ForeignKey(User, blank=False, null=False,related_name="usurioReserva" , on_delete=models.CASCADE)
    viagem = models.ForeignKey(Viagens,blank=False,null=False,related_name="viagemReseva",  on_delete=models.CASCADE)
    dataReserva = models.DateTimeField(),
    valorDiaria = models.ForeignKey(Viagens, blank=False, null=False,related_name="diariaViagem",  on_delete=models.CASCADE)
    dias = models.IntegerField(blank=False, null=False),
    valorFinal = models.DecimalField(null=False,blank=False,max_digits=2,decimal_places=1)
    animal = models.BooleanField(default=False)
    nota = models.DecimalField(null=False, blank=False,max_digits=2,decimal_places=1,validators=[MinValueValidator(0),MaxValueValidator(10)])
    pagamentoId = models.ForeignKey(Pagamentos, blank=False, related_name="pagamentoId",on_delete=models.CASCADE)
    
    def __save__(self, *args, **kwargs):
        self.valorFinal = self.viagem__valorDiaria * self.dias
        super(Reserva, self).__save__(*args, **kwargs)
    
    def __str__(self):
        return self.usuario
    
class Auxiliar(models.Model):
    viagem = models.ForeignKey(Viagens, blank=False, related_name="viagemAuxiliar",on_delete= models.CASCADE)
    status = models.BooleanField(default=False,null=False, blank=False)
    dia = models.DateField(null=False, blank=False,default=timezone.now)
    def __str__(self):
        return self.usuario