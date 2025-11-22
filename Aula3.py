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