from django.db import models


class Guia(models.Model):
    regid = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=100)
    idguia = models.IntegerField()
    srcfecha = models.DateTimeField()
    stsguia = models.IntegerField(default=1)
    srcnombres = models.CharField(max_length=30)
    srcapelluno = models.CharField(max_length=20)
    srcapelldos = models.CharField(max_length=20)
    srctelefono = models.IntegerField()
    srcdireccion = models.CharField(max_length=100)
    dstnombres = models.CharField(max_length=30)
    dstapelluno = models.CharField(max_length=20)
    dstapelldos = models.CharField(max_length=20)
    dsttelefono = models.IntegerField()
    dstdireccion = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    stspago = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    regsts = models.IntegerField(default=1)
    fecha_reg = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.empresa
    