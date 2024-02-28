from django.db import models

# Create your models here.
class Carro(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cor = models.CharField(max_length=100)
    ano = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    #create_at = models.DateField(auto_now_add=True)


    
