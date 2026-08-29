"""
Módulo com as funções do menu.
"""

from time import sleep
from .produtos import lista_produtos

def menu():
    """Exibe o menu principal."""
    print("\n======= Menu: =======")
    print("1. Cadastrar Produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Calcular Total de Produtos em Estoque")
    print("5. Sair")

def cadastrar_produto():
    """Função para cadastrar um novo produto."""
    print("\n--- Cadastro de Produto ---")
    
    while True:
        try:
            codigo = int(input("Digite o código do produto: "))
            for produto in lista_produtos:
                if produto['codigo'] == codigo:
                    print("Erro: Código já cadastrado! Por favor, tente novamente.")
                    break
            else:
                break
        except ValueError:
            print("Erro: Código deve ser um número inteiro!")
    
    nome = input("Digite o nome do produto: ")
    
    while True:
        try:
            preco_input = input("Digite o preço do produto: ")
            preco_input = preco_input.replace(',', '.')
            preco = float(preco_input)
            if preco < 0:
                print("Erro: Preço não pode ser negativo! Tente novamente.")
            else:
                break
        except ValueError:
            print("Erro: Preço deve ser um número decimal!")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("Erro: Quantidade não pode ser negativa! Tente novamente.")
            else:
                break
        except ValueError:
            print("Erro: Quantidade deve ser um número inteiro!")
    
    novo_produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    lista_produtos.append(novo_produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")
    sleep(1)

def remover_produto():
    """Função para remover um produto."""
    print("\n--- Remover Produto ---")
    try:
        codigo = int(input("Digite o código do produto a ser removido: "))
        for produto in lista_produtos:
            if produto['codigo'] == codigo:
                lista_produtos.remove(produto)
                print(f"Produto '{produto['nome']}' removido com sucesso!")
                sleep(1)
                return
        print(f"Produto com código {codigo} não encontrado.")
        sleep(1)
    except ValueError:
        print("Erro: Código deve ser um número inteiro!")
        sleep(1)

def listar_produtos():
    """Função para listar todos os produtos."""
    print("\n--- Lista de Produtos em Estoque ---")
    if lista_produtos:
        print("Código | Nome | Preço | Quantidade")
        print("-" * 40)
        for produto in lista_produtos:
            print(f"{produto['codigo']:6d} | {produto['nome']:10} | R${produto['preco']:6.2f} | {produto['quantidade']:6d}")
    else:
        print("Nenhum produto cadastrado no estoque.")
    sleep(1)

def calcular_total_estoque():
    """Função para calcular o total de produtos em estoque."""
    print("\n--- Total de Produtos em Estoque ---")
    total = 0
    for produto in lista_produtos:
        total += produto['quantidade']
    print(f"Quantidade total de produtos em estoque: {total}")
    sleep(1)
