# tarefas.py
# Aluno de ADS - 2º semestre
# Sistema simples de gerenciamento de tarefas
# Organização em blocos e muitos comentários para mostrar o raciocínio
 
 
import os
from datetime import datetime
 
 
def limpar_tela():
    os.system('cls')
   
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Estruturas    - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
# Estruturas de dados
tarefas = []  # Lista que vai guardar todas as tarefas
 
 
# Prioridades possíveis
prioridades = ["Urgente", "Alta", "Média", "Baixa"]
 
 
# Origens possíveis
origens = ["E-mail", "Telefone", "Chamado do Sistema"]
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Criar Tarefa  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
def criar_tarefa():
    print("\n--- Criar Tarefa ---")
 
 
    titulo = input("Digite o título da tarefa: ")
 
 
    # Escolha da prioridade
    print("Escolha a prioridade:")
    for i, p in enumerate(prioridades, 1):
        print(f"{i} - {p}")
    num_prioridade = int(input("Digite o número da prioridade: "))
    prioridade = prioridades[num_prioridade - 1]
 
 
    # Escolha da origem
    print("Escolha a origem da tarefa:")
    for i, o in enumerate(origens, 1):
        print(f"{i} - {o}")
    num_origem = int(input("Digite o número da origem: "))
    origem = origens[num_origem - 1]
 
 
    # Criando a tarefa
    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
        "status": "Pendente",
        "origem": origem
    }
 
 
    tarefas.append(tarefa)
    print("Tarefa criada com sucesso!")
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Verificação   - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
def verificar_tarefa():
    print("\n--- Verificação de Urgência ---")
 
 
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
 
 
    # Procurar pela ordem de prioridade
    for p in prioridades:
        for t in tarefas:
            if t["prioridade"] == p and t["status"] == "Pendente":
                # Se encontrar, muda para "Fazendo"
                # Primeiro, tira qualquer outra do "Fazendo"
                for outra in tarefas:
                    if outra["status"] == "Fazendo":
                        outra["status"] = "Pendente"
 
 
                t["status"] = "Fazendo"
                print("Tarefa encontrada e colocada como Fazendo:")
                print(t)
                return
    print("Não há tarefas pendentes.")
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Atualizar     - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
def atualizar_prioridade():
    print("\n--- Atualizar Prioridade ---")
 
 
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
 
 
    for i, t in enumerate(tarefas):
        print(i, t)
 
 
    idx = int(input("Digite o índice da tarefa: "))
    print("Escolha a nova prioridade:")
    for i, p in enumerate(prioridades, 1):
        print(f"{i} - {p}")
    num_prioridade = int(input("Digite o número da nova prioridade: "))
    tarefas[idx]["prioridade"] = prioridades[num_prioridade - 1]
 
 
    print("Prioridade atualizada com sucesso!")
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Concluir      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
def concluir_tarefa():
    print("\n--- Concluir Tarefa ---")
 
 
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
 
 
    for i, t in enumerate(tarefas):
        print(i, t)
 
 
    idx = int(input("Digite o índice da tarefa: "))
    tarefas[idx]["status"] = "Concluída"
    tarefas[idx]["conclusao"] = datetime.now().strftime("%d/%m")
 
 
    print("Tarefa concluída com sucesso!")
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Relatório     - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
def relatorio():
    print("\n--- Relatório de Tarefas ---")
 
 
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
 
 
    for t in tarefas:
        print(t)
 
 
 
# ======================================================================
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Menu Principal - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Criar tarefa")
        print("2 - Verificar tarefa")
        print("3 - Atualizar prioridade")
        print("4 - Concluir tarefa")
        print("5 - Relatório")
        print("6 - Limpar tela")
        print("0 - Sair")
 
 
        opcao = int(input("Digite a opção: "))
 
 
        if opcao == 1:
            criar_tarefa()
        elif opcao == 2:
            verificar_tarefa()
        elif opcao == 3:
            atualizar_prioridade()
        elif opcao == 4:
            concluir_tarefa()
        elif opcao == 5:
            relatorio()
        elif opcao == 6:
            limpar_tela()
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")
 
 
 
# Execução do programa
menu()