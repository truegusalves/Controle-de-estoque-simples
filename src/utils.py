"""
Módulo com funções utilitárias.
"""

from time import sleep

def mensagem_saida():
    """Exibe mensagem de saída do sistema."""
    print("Saindo do sistema. Até logo!")
    for i in range(5):
        print(".", end="", flush=True)
        sleep(0.5)
    print()
