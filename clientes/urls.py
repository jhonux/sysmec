from django.urls import path
from . import views


urlpatterns = [
     path('', views.clientes, name="clientes"),
     path('clientes_lista/', views.clientes_lista, name="clientes_lista"),
     path('cadastro_clientes/', views.cadastro_clientes, name="cadastro_clientes"),
     path('informacoes_cliente/<int:cliente_id>', views.informacoes_cliente, name="informacoes_cliente"),
     path('editar_cliente/<int:cliente_id>', views.editar_cliente, name="editar_cliente"),
     path('excluir_cliente/<int:cliente_id>', views.excluir_cliente, name="excluir_cliente"),
     path('exportar_clientes/', views.exportar_clientes, name="exportar_clientes"),
     # path('criar_novo_orcamento/', views.criar_novo_orcamento, name='criar_novo_orcamento'),

     # path('buscar_cliente_por_nome/', views.buscar_cliente_por_nome, name='buscar_cliente_por_nome'),
     path('novo_orcamento/', views.novo_orcamento, name="novo_orcamento"),
     path('criar_orcamento/<int:cliente_id>/', views.criar_orcamento, name='criar_orcamento'),
     path('contar_orcamentos/', views.contar_orcamentos_nao_aprovados, name='contar_orcamentos'),
     path('orcamentos_lista/', views.orcamentos_lista, name='orcamentos_lista'),
     path('orcamentos_abertos/', views.orcamentos_abertos, name='orcamentos_abertos'),
     path('excluir_orcamento/<int:orcamento_id>/', views.excluir_orcamento, name='excluir_orcamento'),
     path('os_aberta/<int:orcamento_id>/', views.os_aberta, name='os_aberta'),


     path('ordem_servico/', views.ordem_servico, name='ordem_servico'),
     path('ordem_lista/', views.ordem_lista, name='ordem_lista'),


]
