from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Subastado(models.Model):
    titulo=models.Charfield(max_lenth=64)
    descripcion=models.Charfield(max_lenth=300)
    puja_actual=models.FloatField()
    numero_pujas=models.IntegerField(min_value=0)
    autor=models.ForeignKey(User, related_name="vendedor")
    

class comentarios(models.Model):
    usuario=models.ManyToManyField(User,blank=True, related_name="comentador")
    comentario=models.Charfield(max_lenth=300)

class pujas(models.Model):
    pass