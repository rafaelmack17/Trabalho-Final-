================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 1  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 1 - Média de Filmes Avaliados
avaliacoes = [8, 7, 9, 6, 10]
soma_avaliacoes = 0

for nota in avaliacoes:
    soma_avaliacoes += nota

media = soma_avaliacoes / len(avaliacoes)
print("Média das avaliações:", media)

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 2  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 2 - Playlist de Música
playlist = ["Música A", "Música B", "Música C", "Música D", "Música E"]
musica_procurada = "Música C"

if musica_procurada in playlist:
    print("Música encontrada na playlist!")
else:
    print("Música não disponível.")

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 3  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 3 - Registro de Pedidos
pedidos_do_dia = ["pizza", "hambúrguer", "refrigerante", "pizza"]
print("Quantidade total de pedidos:", len(pedidos_do_dia))

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 4  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 4 - Lista de Convidados
convidados = ["Ana", "Bruno", "Carlos", "Diana"]
for pessoa in convidados:
    print("Convidado:", pessoa)

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 5  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 5 - Histórico de Navegação
historico = ["google.com", "youtube.com", "wikipedia.org"]
historico.append("openai.com")
print("Histórico completo:", historico)

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 6  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 6 - Login de Usuário
usuarios_validos = ["pedro", "joao", "maria", "ana", "lucas"]
usuario_digitado = "maria"

acesso = False
for usuario in usuarios_validos:
    if usuario == usuario_digitado:
        acesso = True
        break

if acesso:
    print("Acesso concedido!")
else:
    print("Usuário não encontrado.")

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 7  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 7 - Conversor de Distâncias

distancias_km = [2, 5, 10, 21, 50]
distancias_milhas = []

for km in distancias_km:
    milhas = km * 0.621371
    distancias_milhas.append(milhas)

print("Distâncias em KM:", distancias_km)
print("Distâncias em Milhas:", distancias_milhas)

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 8  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 8 - Inventário de Itens
inventario = ("maçã", 10, "caixa", 5, "banana", 12)
total_itens = 0

for item in inventario:
    if isinstance(item, int):
        total_itens += item

print("Total de itens no inventário:", total_itens)

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 9  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 9 - Busca em Lista Ordenada
numeros_ordenados = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
numero_procurado = 4
contador = 0

for numero in numeros_ordenados:
    if numero == numero_procurado:
        contador += 1

if contador > 0:
    print(f"Número encontrado e ele apareceu {contador} vezes.")
else:
    print("Número não encontrado na lista.")

# ================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 10 - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
# Exercício 10 - Classificador de Notas
notas_turma = [5, 7, 8, 6, 10, 3, 9, 4, 7, 2]
aprovados = []
reprovados = []

for nota in notas_turma:
    if nota >= 7:
        aprovados.append(nota)
    else:
        reprovados.append(nota)

print("Aprovados:", aprovados)
print("Reprovados:", reprovados)