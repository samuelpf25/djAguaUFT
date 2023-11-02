from django.urls import path
from .views import index,form_solicitacao

urlpatterns = [
    path('', index),
    path('solicitacao/', form_solicitacao, name='form_solicitacao'),
]
