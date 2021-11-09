from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey

# Create your models here

class TipoDispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creada = models.DateField(auto_now_add=True)

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creada = models.DateField(auto_now_add=True)

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creada = models.DateField(auto_now_add=True)

class TipoCaso(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creada = models.DateField(auto_now_add=True)

class Caso(models.Model):
    descripcion = models.CharField(max_length=250)
    id_tipo_dispositivo = ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    id_marca = ForeignKey(Marca, on_delete=models.CASCADE)
    id_modelo = ForeignKey(Modelo, on_delete=models.CASCADE)
    id_tipo_caso = ForeignKey(TipoCaso, on_delete=models.CASCADE)
    nombre_cliente = CharField(max_length=100)
    telefono_cliente = CharField(max_length=8)
    direccion_cliente = CharField(max_length=250)
    estado_caso = CharField(max_length=60)
    fecha_recibido = models.DateField()
    fecha_entregado = models.DateField()
    monto = FloatField(default=0)