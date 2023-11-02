from django.contrib import admin
from .models import *

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome_campus',)

@admin.register(Predio)
class PredioAdmin(admin.ModelAdmin):
    list_display = ('nome_predio','criado','modificado')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome_sala','tipo_ambiente','criado_sala','modificado_sala')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario','telefone','id_sala','criado','modificado')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_colaborador','telefone','criado','modificado')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','id_sala','qtd','data','id_colaborador','criado','modificado')