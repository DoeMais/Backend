from rest_framework import routers
from .viewsets import ProdutosViewSets, UsuariosViewSets

produto_routers = routers.DefaultRouter()
produto_routers.register(r'/produtos',ProdutosViewSets)
produto_routers.register(r'/usuarios',UsuariosViewSets)
urlpatterns = produto_routers.urls
 