from django.db import models


class Campus(models.Model):
    nome_campus = models.CharField('Campus', max_length=100)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    def __str__(self):
        return self.nome_campus
class Predio(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    nome_predio = models.CharField('Nome prédio', max_length=100)
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Predio'
        verbose_name_plural = 'Predios'

    def __str__(self):
        return self.nome_predio
class Sala(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    tipo = (
        ('Sala de Aula', 'Sala de Aula'),
        ('Laboratório', 'Laboratório'),
        ('Banheiro', 'Banheiro'),
    )
    nome_sala = models.CharField('Nome sala', max_length=100)
    tipo_ambiente = models.CharField('Tipo de Ambiente', choices=tipo, max_length=100)
    criado_sala = models.DateField('Data de Criação', auto_now_add=True)
    modificado_sala = models.DateField('Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return f"{self.predio}, {self.nome_sala}"
class Usuario(models.Model):
    nome_usuario = models.CharField('Nome usuário', max_length=100)
    telefone = models.IntegerField('Telefone')
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome_usuario
class Colaborador(models.Model):
    nome_colaborador = models.CharField('Nome colaborador', max_length=100)
    telefone = models.IntegerField('Telefone')
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome_colaborador

class Pedido(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE, default=None)
    qtd = models.IntegerField('Quantidade')
    data = models.DateField('Data de Entrega')
    id_colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True)
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.pk)

def __str__(self):
    return self.nome
