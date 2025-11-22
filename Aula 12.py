print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 1      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
with open('saudacao.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Olá, Mundo!')
 
 
print("Arquivo 'saudacao.txt' criado e conteúdo escrito com sucesso!\n")
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 2      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
with open('saudacao.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
 
 
print("Conteúdo lido do arquivo:")
print(conteudo + '\n')
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 3      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
nomes_alunos = ["João", "Maria", "Pedro", "Ana"]
with open('lista_alunos.txt', 'w', encoding='utf-8') as arquivo:
    for nome in nomes_alunos:
        arquivo.write(nome + '\n')
 
 
print("Arquivo 'lista_alunos.txt' criado com lista de alunos.\n")
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 4      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
with open('lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(f"Aluno encontrado: {linha.strip()}")
print()
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 5      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
novo_nome = "Novo Aluno"
with open('lista_alunos.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(novo_nome + '\n')
 
 
print("Novo aluno adicionado! Conteúdo atualizado:")
with open('lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
print()
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 6      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
with open('saudacao.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('O conteúdo anterior foi deletado!')
 
 
with open('saudacao.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
print()
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 7      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
with open('lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
 
 
print(f"Total de alunos encontrados: {len(linhas)}\n")
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 8      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
with open('lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
    nomes = arquivo.readlines()
 
 
nomes_modificados = [f"ID-{nome.strip()}\n" for nome in nomes]
 
 
with open('lista_alunos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(nomes_modificados)
 
 
print("Arquivo modificado com prefixos 'ID-':")
with open('lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
print()
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 9      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
with open('lista_alunos.txt', 'r', encoding='utf-8') as origem, open('alunos_filtrados.txt', 'w', encoding='utf-8') as destino:
    for linha in origem:
        if 'a' in linha.lower():
            destino.write(linha)
 
 
print("Arquivo 'alunos_filtrados.txt' criado com nomes filtrados:")
with open('alunos_filtrados.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
print()
 
 
 
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercício 10     - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
def adicionar_novo_item(item):
    with open('itens.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(item + '\n')
 
 
 
aAdicionar = ['Item 1', 'Item 2', 'Item 3']
for i in aAdicionar:
    adicionar_novo_item(i)
 
 
 
def ler_itens():
    with open('itens.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
 
 
print("Itens adicionados com sucesso! Conteúdo atual do arquivo:")
ler_itens()