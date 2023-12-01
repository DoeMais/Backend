from rest_framework import routers
from .viewsets import PublicacaoViewSets, UsuariosViewSets , DoacoesViewSets

dados_routers = routers.DefaultRouter()
dados_routers.register(r'/publicacoes',PublicacaoViewSets)
dados_routers.register(r'/doacoes',DoacoesViewSets)
dados_routers.register(r'/usuarios',UsuariosViewSets)
urlpatterns = dados_routers.urls
 