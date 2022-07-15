from sqlite3 import adapt
from django.contrib import admin

from .models import Avaria, Avatar_Carro, Carro, Doc, Doc_Revendedor, Revendedor, Visita

# Register your models here.
@admin.register(Revendedor)
class RevendedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_primary', 'phone_secondary', 'email', 'bi', 'avatar')


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'cor', 'matricula', 'modelo', 'tipo_motor', 'estado')


@admin.register(Avaria)
class AvariaAdmin(admin.ModelAdmin):
    list_display = ('carro', 'designacao', 'descricao')


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('carro', 'nome', 'phone_primary', 'phone_secondary', 'data_visita')


@admin.register(Avatar_Carro)
class AvatarCarroAdmin(admin.ModelAdmin):
    list_display = ('carro', 'designacao', 'descricao')


@admin.register(Doc_Revendedor)
class DocRevendedorAdmin(admin.ModelAdmin):
    list_display = ('revendedor', 'designation', 'description', 'avatar')
