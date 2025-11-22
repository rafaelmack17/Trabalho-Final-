print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 1 - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 1 - Criação de Matriz 2x2
matriz_2x2 = [
[1, 2],
[3, 4]
]
print("Matriz 2x2:")
for linha in matriz_2x2:
print(linha)


# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 2 - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 2 - Acessando elemento pela posição
matriz_3x3 = [
[5, 8, 10],
[3, 6, 12],
[7, 9, 4]
]
print("Item na 2ª linha, 3ª coluna:", matriz_3x3[1][2])


# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 3 - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 3 - Matriz vazia + entrada de usuário
matriz_compras = []
for i in range(3):
produto = input("Digite o nome do produto: ")
quantidade = input("Digite a quantidade: ")
valor = input("Digite o valor: ")
matriz_compras.append([produto, quantidade, valor])


print("Matriz final de compras:")
print(matriz_compras)


# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 4 - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 4 - Matriz com textos
matriz_textos = [
["maçã", "banana"],
["carro", "moto"]
]


for linha in matriz_textos:
for item in linha:
print(item)


# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 5 - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 5 - Soma de elementos
vendas = [
[10, 20],
[15, 30]
]
total = 0


for linha in vendas:
for valor in linha:
total += valor


print("Total das vendas:", total)


# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 6 - - -")
print(tabuleiro[i][j])

print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Desafio      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
import os
 
 
# Cria o tabuleiro 3x3 com traços
tabuleiro = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
 
 
# Laço para 9 jogadas
for jogada in range(9):
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
 
 
    # Mostra o tabuleiro
    print("Tabuleiro atual:")
    for linha in tabuleiro:
        print(linha)
 
 
    # Alterna o jogador
    if jogada % 2 == 0:
        jogador = 'X'
    else:
        jogador = 'O'
 
 
    print("\nVez do jogador", jogador)
 
 
    # Pede a jogada
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))
 
 
    # Verifica se a posição está livre
    if tabuleiro[linha][coluna] == '-':
        tabuleiro[linha][coluna] = jogador
    else:
        print("Essa posição já está ocupada! Tente novamente.")
        input("Pressione Enter para continuar...")
        continue
 
 
# Mostra o tabuleiro final
os.system('cls' if os.name == 'nt' else 'clear')
print("Fim do jogo! Tabuleiro final:")
for linha in tabuleiro:
    print(linha)