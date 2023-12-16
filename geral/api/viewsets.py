from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from  geral.api import serializers
from geral import models
from ..models import Publicacao , Doacoes , Usuario
from django.views.decorators.http import require_GET


class PublicacaoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class =  serializers.PublicacaoSerializers
    queryset = models.Publicacao.objects.all()

def get_queryset(self): 
    query = Publicacao.objects.all()
    nome = self.request.query_params.get('nome')
    if nome is not None: 
        query = query.filter(nome_icontains = nome)
    return query

class DoacoesViewSets(viewsets.ModelViewSet):
<<<<<<< Updated upstream
    permission_classes = (IsAuthenticated)

=======
    permission_classes = (IsAuthenticated,)
>>>>>>> Stashed changes
    serializer_class =  serializers.DoacoesSerializers
    queryset = models.Doacoes.objects.all()

def get_queryset(self): 
    query = DoacoesViewSets.objects.all()
    titulo_geral = self.request.query_params.get('titulo_geral')
    if titulo_geral is not None: 
        query = query.filter(nome_icontains = titulo_geral)
    return query


class UsuariosViewSets(viewsets.ModelViewSet):
    serializer_class =  serializers.UsuariosSerializers
    queryset = models.Usuario.objects.all()

@require_GET
def query(request):
   nome_usuario = request.GET['nome']
   email_usuario =  request.GET['email']
   senha_usuario =  request.GET['senha']
   idade_usuario = request.GET['idade']

   novoUsuario = Usuario.objects.create_user(nomeUser = nome_usuario , emailUser = email_usuario, senhaUser = senha_usuario , idadeUser = idade_usuario  )
   novoUsuario.save()
   
   

    