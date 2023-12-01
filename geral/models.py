from django.db import models
from uuid import uuid4

def upload_media(instance , filename):
   return f"publicacao/{instance.id_publicacao}-{filename}"

def upload_media2(instance , filename):
   return f"doacao/{instance.id_doacoes}-{filename}"
   
def upload_media3(instance , filename):
   return f"user/{instance.id_user}-{filename}"

class Publicacao(models.Model):
   id_publicacao = models.UUIDField(primary_key=True, default=uuid4 ,  editable=False)
   nome = models.CharField(max_length=255)
   endereco =  models.CharField(max_length=254)
   texto_explicativo = models.TextField()
   image_P = models.ImageField(upload_to= upload_media, blank = True, null = True)


   def __str__(self):
      return self.nome
   
class Doacoes(models.Model):
   id_doacoes = models.UUIDField(primary_key=True, default=uuid4, editable=False)
   titulo_geral = models.CharField(max_length=255)
   contato =  models.CharField(max_length=254)
   texto_explicativo = models.TextField()
   image_D = models.ImageField(upload_to= upload_media2, blank = True, null = True)

   def __str__(self):
      return self.titulo_geral
        
class Usuario(models.Model): 
      id_user = models.UUIDField(primary_key=True, default=uuid4 , editable = False)
      nomeUser = models.TextField(max_length=255)
      emailUser = models.EmailField(max_length=255, unique = True)
      senhaUser = models.CharField(max_length=255)
      image_User = models.ImageField(upload_to= upload_media3, blank = True, null = True)

   

      USERNAME_FIELD = 'emailUser'
      REQUIRED_FIELDS = ['nomeUser','senhaUser', 'idadeUser']

      def __str__(self):
         return self.nomeUser
      
      