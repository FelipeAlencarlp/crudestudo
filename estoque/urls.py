from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('visualizar_produto/<int:id>', views.visualizar_produto, name='visualizar_produto'),
    path('editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('excluir_produto/<int:id>', views.excluir_produto, name='excluir_produto'),
]