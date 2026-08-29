"""
Pacote do sistema de controle de estoque.
"""

from .menu import menu, cadastrar_produto, remover_produto, listar_produtos, calcular_total_estoque
from .utils import mensagem_saida
from .produtos import lista_produtos

__all__ = [
    'menu',
    'cadastrar_produto',
    'remover_produto', 
    'listar_produtos',
    'calcular_total_estoque',
    'mensagem_saida',
    'lista_produtos'
]
