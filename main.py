#!/usr/bin/env python3

from time import sleep
from src import menu, cadastrar_produto, remover_produto, listar_produtos, calcular_total_estoque, mensagem_saida

def main():
    """Função principal do programa."""
    print('Bem-vindo ao Sistema de Controle de Estoque!')
    
    while True:
        menu()
        print("")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_produto()
        
        elif opcao == '2':
            remover_produto()
        
        elif opcao == '3':
            listar_produtos()
        
        elif opcao == '4':
            calcular_total_estoque()
        
        elif opcao == '5':
            mensagem_saida()
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")
            sleep(1)

if __name__ == "__main__":
    main()