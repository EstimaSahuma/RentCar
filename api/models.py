from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Revendedor(models.Model):
    #user = models.ForeignKey(user, related_name='is_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    bi = models.CharField(max_length=15, unique=True)#Number identification to people
    avatar = models.ImageField(upload_to = 'images')

    class Meta:
        verbose_name = 'Revendedor'
        verbose_name_plural = 'Revendedores'
        ordering = ['id']


class User_Revendedor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    revendedor = models.ForeignKey(Revendedor, on_delete=models.CASCADE)


class Carro(models.Model):
    #revendedor = models.ForeignKey(Revendedor, related_name='carros', on_delete=models.CASCADE)
    marca = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    tipo_motor = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['id']


class Avaria(models.Model):
    carro = models.ForeignKey(Carro, related_name='avarias', on_delete=models.CASCADE)
    designacao = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Avaria'
        verbose_name_plural = 'Avarias'
        ordering = ['id']


class Avatar_Carro(models.Model):
    carro = models.ForeignKey(Carro, related_name='avatar_carroes', on_delete=models.CASCADE)
    designacao = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']


class Visita(models.Model):
    carro = models.ForeignKey(Carro, related_name='visitas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20)
    data_visita = models.DateTimeField()

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ['id']


class Doc(models.Model):
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to = 'images')

    class Meta:
        abstract = True


class Doc_Revendedor(Doc):
    revendedor = models.ForeignKey(Revendedor, related_name='doc_revendedores', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class Doc_Carro(Doc):
    carro = models.ForeignKey(Carro, related_name='doc_carros', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

""" Proposta de carro sera uma classe com a de visita """
