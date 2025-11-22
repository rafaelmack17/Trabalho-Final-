print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 1  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 1
 
 
nomes = ["Ana", "Bruno", "Carla"]
notas = [9, 6, 8]
 
 
for i in range(len(nomes)):
    media = notas[i]
    if media >= 7:
        print(f"{nomes[i]} foi aprovado com média {media}.")
    else:
        print(f"{nomes[i]} foi reprovado com média {media}.")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 2  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 2
 
 
 
anos_nascimento = [2005, 2010, 1998, 2007]
ano_atual = 2024
 
 
 
for ano in anos_nascimento:
    idade = ano_atual - ano
    if idade >= 18:
        print(f"Quem nasceu em {ano} tem {idade} anos e é maior de idade.")
    else:
        print(f"Quem nasceu em {ano} tem {idade} anos e é menor de idade.")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 3  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 3
 
 
 
pares = 0
impares = 0
 
 
 
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 22, 23, 24, 25)
 
 
 
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
 
 
 
print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")
print(f"Total de números analisados: {len(numeros)}")
 
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 4  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 4
 
 
 
turma_a = ["João", "Maria", "Jibinba", "Ana", "Lucas"]
turma_b = ["Carlos", "Fernanda", "Rafael", "Camila", "Gustavo"]
 
 
 
nome_aluno = "Jibinba" 
 
 
 
if nome_aluno in turma_a:
    print(f"O aluno {nome_aluno} está na Turma A.")
    print(f"Total de alunos na Turma A: {len(turma_a)}")
elif nome_aluno in turma_b:
    print(f"O aluno {nome_aluno} está na Turma B.")
    print(f"Total de alunos na Turma B: {len(turma_b)}")
else:
    print(f"O aluno {nome_aluno} não foi encontrado.")
 
 
    
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 5  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 5
 
 
 
tarefas = ["Estudar Python", "Fazer exercícios", "Ler um livro", "Meditar"]
print(f"Lista inicial: {tarefas}")
 
 
 
tarefas.append("Comprar pão")
tarefas.remove("Estudar Python")
 
 
 
print(f"Lista atualizada: {tarefas}")

print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 1  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 1
import random
import string
 
 
senhas = []
quantidade = int(input("Digite a quantidade de senhas que devem ser geradas: "))
 
 
caracteres = string.digits * 7 + string.ascii_letters * 3
 
 
for _ in range(quantidade):
    senha = "".join(random.sample(caracteres, 10))
    senhas.append(senha)
 
 
print("\nSenhas geradas:", senhas)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 2  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 2
vendas = [150.75, 200.50, 50.00, 320.10, 180.95]
 
 
total_vendas = sum(vendas)
 
 
vendedor_a = total_vendas * 0.60
vendedor_b = total_vendas * 0.40
 
 
print(f"Valor total de vendas do dia: R$ {total_vendas:.2f}")
print(f"Vendedor A (60%): R$ {vendedor_a:.2f}")
print(f"Vendedor B (40%): R$ {vendedor_b:.2f}")
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 3  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 3
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Cadeira", "Mesa"]
 
 
produtos_filtrados = [p for p in produtos if 'a' in p.lower()]
 
 
print("Produtos que contêm a letra 'a':")
print(produtos_filtrados)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 4  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 4
eventos = [("Reunião de Equipe", "15/09/2025"), ("Treinamento", "20/09/2025")]
 
 
nome_evento = input("Digite o nome do evento: ")
data_evento = input("Digite a data do evento (DD/MM/AAAA): ")
 
 
eventos.append((nome_evento, data_evento))
 
 
print("\nLista completa de eventos:")
for nome, data in eventos:
    print(f"Evento: {nome}, Data: {data}")
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 5  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
#Codigos exercicio 5
from collections import Counter
 
 
votos = [1, 2, 1, 3, 2, 3, 2, 1, 1, 3, 2, 3]
 
 
# A classe Counter cria um dicionário com a contagem dos votos
contagem_votos = Counter(votos)
 
 
print("Resultado da apuração:")
print(f"Candidato 1: {contagem_votos.get(1, 0)} votos")
print(f"Candidato 2: {contagem_votos.get(2, 0)} votos")
print(f"Candidato 3: {contagem_votos.get(3, 0)} votos")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio   - - -")
print("- - - - - - - - - - - - - - - - - - - - -")