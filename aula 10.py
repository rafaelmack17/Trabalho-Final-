# ==============================================================================
# Variáveis Globais [cite: 39, 40, 55]
# ==============================================================================
 
 
lista_de_tarefas = []
PRIORIDADES_VALIDAS = ["Urgente", "Alta", "Média", "Baixa"]
STATUS_VALIDOS = ["Pendente", "Fazendo", "Concluída"]
ORIGENS_VALIDAS = ["E-mail", "Telefone", "Chamado do Sistema"]
tarefa_em_execucao = None # Somente uma tarefa deve estar em execução por vez [cite: 11]
 
 
# ==============================================================================
# Funções [cite: 42, 43, 56]
# ==============================================================================
 
 
def validar_input(prompt, opcoes_validas):
    entrada = ""
    while entrada not in opcoes_validas:
        print(f"\nOpções disponíveis: {', '.join(opcoes_validas)}")
        entrada = input(prompt).strip()
        if entrada not in opcoes_validas:
            print(f"Erro: '{entrada}' não é uma opção válida. Tente novamente.")
    return entrada
 
 
 
def criar_tarefa(): # 1. Criação [cite: 20]
    global lista_de_tarefas
    print("\n--- 1. Criar Nova Tarefa ---")
    titulo = input("Título (o que deve ser feito?): ").strip()
    prioridade = validar_input("Prioridade (Urgente, Alta, Média, Baixa): ", PRIORIDADES_VALIDAS)
    origem = validar_input("Origem da Tarefa (E-mail, Telefone, Chamado do Sistema): ", ORIGENS_VALIDAS)
 
 
    nova_tarefa = {
        "Título": titulo,
        "Prioridade": prioridade,
        "Status": "Pendente",  # Status deve começar como "Pendente" [cite: 15]
        "Origem da Tarefa": origem,
        "Data de Conclusão": None
    }
 
 
    lista_de_tarefas.append(nova_tarefa)
    print(f"\n[SUCESSO] Tarefa '{titulo}' criada.")
 
 
 
def verificar_e_pegar_tarefa(): # 2. Verificação de Urgência [cite: 22, 23]
    global tarefa_em_execucao, lista_de_tarefas
    print("\n--- 2. Selecionar Tarefa ---")
 
 
    if tarefa_em_execucao is not None:
        print(f"[ALERTA] Já existe uma tarefa em execução: '{tarefa_em_execucao['Título']}'.")
        return
 
 
    for prioridade_alvo in PRIORIDADES_VALIDAS:
        tarefa_encontrada = next(
            (t for t in lista_de_tarefas if t["Status"] == "Pendente" and t["Prioridade"] == prioridade_alvo), 
            None
        )
 
 
        if tarefa_encontrada:
            tarefa_encontrada["Status"] = "Fazendo" # Status atualizado para "Fazendo" [cite: 25]
            tarefa_em_execucao = tarefa_encontrada
            print(f"[SUCESSO] Tarefa selecionada: '{tarefa_encontrada['Título']}'. Status: 'Fazendo'.")
            return
        
    print("[INFO] Não há tarefas pendentes na lista.")
 
 
 
def atualizar_prioridade(): # 3. Atualização de Prioridade [cite: 26]
    global lista_de_tarefas
    print("\n--- 3. Atualizar Prioridade ---")
    
    if not lista_de_tarefas:
        print("[INFO] Nenhuma tarefa para atualizar.")
        return
 
 
    print("Tarefas Disponíveis para Atualização:")
    for i, tarefa in enumerate(lista_de_tarefas):
        print(f"  [{i}] Título: {tarefa['Título']} | Prioridade Atual: {tarefa['Prioridade']}")
 
 
    try:
        indice = int(input("Digite o NÚMERO da tarefa: "))
        if 0 <= indice < len(lista_de_tarefas):
            tarefa = lista_de_tarefas[indice]
            prioridade_antiga = tarefa["Prioridade"]
            nova_prioridade = validar_input("Nova Prioridade (Urgente, Alta, Média, Baixa): ", PRIORIDADES_VALIDAS)
            tarefa["Prioridade"] = nova_prioridade
            print(f"[SUCESSO] Prioridade de '{tarefa['Título']}' alterada para '{nova_prioridade}'.")
        else:
            print("[ERRO] Índice inválido.")
    except ValueError:
        print("[ERRO] Entrada inválida.")
 
 
 
def concluir_tarefa(): # 4. Conclusão das tarefas [cite: 27, 28]
    global tarefa_em_execucao
    print("\n--- 4. Concluir Tarefa ---")
 
 
    if tarefa_em_execucao is None:
        print("[INFO] Nenhuma tarefa está em execução.")
        return
 
 
    tarefa_em_execucao["Data de Conclusão"] = datetime.now()
    tarefa_em_execucao["Status"] = "Concluída"
    
    print(f"[SUCESSO] Tarefa '{tarefa_em_execucao['Título']}' concluída em: {tarefa_em_execucao['Data de Conclusão'].strftime('%Y-%m-%d %H:%M:%S')}")
    tarefa_em_execucao = None
 
 
 
def excluir_concluidas_antigas(): # 5. Exclusão de Concluídas Antigas [cite: 29]
    global lista_de_tarefas
    print("\n--- 5. Excluir Concluídas Antigas ---")
    
    data_limite = datetime.now() - timedelta(weeks=1)
    
    tarefas_mantidas = [] 
    tarefas_excluidas_count = 0
    
    for tarefa in lista_de_tarefas:
        # Verifica se o status é Concluída E se a data existe E se é mais antiga que o limite
        if tarefa["Status"] == "Concluída" and tarefa["Data de Conclusão"] and tarefa["Data de Conclusão"] < data_limite:
            tarefas_excluidas_count += 1
        else:
            tarefas_mantidas.append(tarefa)
            
    lista_de_tarefas = tarefas_mantidas
    
    if tarefas_excluidas_count > 0:
        print(f"[SUCESSO] {tarefas_excluidas_count} tarefa(s) concluída(s) antiga(s) excluída(s).")
    else:
        print("[INFO] Nenhuma tarefa concluída antiga para excluir.")
 
 
 
def exibir_relatorio(): # 6. Relatório [cite: 30]
    print("\n--- 6. Relatório de Tarefas ---")
 
 
    if not lista_de_tarefas:
        print("[INFO] A lista de tarefas está vazia.")
        return
 
 
    for i, tarefa in enumerate(lista_de_tarefas):
        data_conc = tarefa['Data de Conclusão'].strftime('%Y-%m-%d %H:%M:%S') if tarefa['Data de Conclusão'] else "N/A"
        
        print(f"\nID: {i}")
        print(f"  Título: {tarefa['Título']}") 
        print(f"  Status: {tarefa['Status']}")
        print(f"  Data de Conclusão: {data_conc}")
 
 
 
def menu_principal(): # 1. Menu Principal [cite: 35, 36]
    while True:
        print("\n\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Criar Nova Tarefa")
        print("2. Pegar Próxima Tarefa (Verificar Urgência)")
        print("3. Atualizar Prioridade de Tarefa")
        print("4. Concluir Tarefa em Execução")
        print("5. Excluir Concluídas Antigas (> 1 semana)")
        print("6. Exibir Relatório de Tarefas")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            criar_tarefa()
        elif escolha == '2':
            verificar_e_pegar_tarefa()
        elif escolha == '3':
            atualizar_prioridade()
        elif escolha == '4':
            concluir_tarefa()
        elif escolha == '5':
            excluir_concluidas_antigas()
        elif escolha == '6':
            exibir_relatorio()
        elif escolha == '7':
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida.")
 
 
# ==============================================================================
# Corpo Principal [cite: 58]
# ==============================================================================
 
 
if __name__ == "__main__":
    menu_principal()