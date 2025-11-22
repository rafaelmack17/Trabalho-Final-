# Variáveis Globais
lista_de_tarefas = []
PRIORIDADES_VALIDAS = ["Urgente", "Alta", "Média", "Baixa"]
STATUS_VALIDOS = ["Pendente", "Fazendo", "Concluída"]
ORIGENS_VALIDAS = ["E-mail", "Telefone", "Chamado do Sistema"]
tarefa_em_execucao = None
id_contador = 1  # Para gerar IDs únicos [Tópico 11]
 
 
# Funções
 
 
def validar_input(prompt, opcoes_validas):
    """Validação de entrada textual"""
    print("Executando a função validar_input")  # [Tópico 10]
    entrada = ""
    while entrada not in opcoes_validas:
        print(f"\nOpções disponíveis: {', '.join(opcoes_validas)}")
        entrada = input(prompt).strip()
        if entrada not in opcoes_validas:
            print(f"[ERRO] '{entrada}' não é uma opção válida. Tente novamente.")
    return entrada
 
 
 
def validar_texto_nao_vazio(prompt):
    """Validação de texto lógico e não vazio (1ª Defesa - Validação Lógica)"""
    print("Executando a função validar_texto_nao_vazio")  # [Tópico 10]
    while True:
        texto = input(prompt).strip()
        if texto:
            return texto
        print("[ERRO] O campo não pode estar vazio. Tente novamente.")
 
 
 
def criar_tarefa():
    """Criação de nova tarefa"""
    print("Executando a função criar_tarefa")  # [Tópico 10]
    global lista_de_tarefas, id_contador
    print("\n--- 1. Criar Nova Tarefa ---")
 
 
    titulo = validar_texto_nao_vazio("Título (o que deve ser feito?): ")
    prioridade = validar_input("Prioridade (Urgente, Alta, Média, Baixa): ", PRIORIDADES_VALIDAS)
    origem = validar_input("Origem da Tarefa (E-mail, Telefone, Chamado do Sistema): ", ORIGENS_VALIDAS)
 
 
    nova_tarefa = {
        "ID": id_contador,  # Identificação única [Tópico 11]
        "Título": titulo,
        "Prioridade": prioridade,
        "Status": "Pendente",
        "Origem da Tarefa": origem,
        "Data de Conclusão": None
    }
 
 
    lista_de_tarefas.append(nova_tarefa)
    print(f"\n[SUCESSO] Tarefa '{titulo}' criada com ID {id_contador}.")
    id_contador += 1
 
 
 
def verificar_e_pegar_tarefa():
    """Seleciona próxima tarefa conforme urgência"""
    print("Executando a função verificar_e_pegar_tarefa")  # [Tópico 10]
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
            tarefa_encontrada["Status"] = "Fazendo"
            tarefa_em_execucao = tarefa_encontrada
            print(f"[SUCESSO] Tarefa selecionada: '{tarefa_encontrada['Título']}'. Status: 'Fazendo'.")
            return
 
 
    print("[INFO] Não há tarefas pendentes na lista.")
 
 
 
def atualizar_prioridade():
    """Atualiza prioridade de uma tarefa"""
    print("Executando a função atualizar_prioridade")  # [Tópico 10]
    global lista_de_tarefas
    print("\n--- 3. Atualizar Prioridade ---")
 
 
    if not lista_de_tarefas:
        print("[INFO] Nenhuma tarefa para atualizar.")
        return
 
 
    print("Tarefas Disponíveis:")
    for tarefa in lista_de_tarefas:
        print(f"  [ID: {tarefa['ID']}] {tarefa['Título']} | Prioridade Atual: {tarefa['Prioridade']}")
 
 
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
        tarefa = next((t for t in lista_de_tarefas if t["ID"] == id_tarefa), None)
        if tarefa:
            nova_prioridade = validar_input("Nova Prioridade (Urgente, Alta, Média, Baixa): ", PRIORIDADES_VALIDAS)
            tarefa["Prioridade"] = nova_prioridade
            print(f"[SUCESSO] Prioridade de '{tarefa['Título']}' alterada para '{nova_prioridade}'.")
        else:
            print("[ERRO] Nenhuma tarefa encontrada com esse ID.")
    except ValueError:
        print("[ERRO] Entrada inválida. Digite apenas números.")
 
 
 
def concluir_tarefa():
    """Conclui a tarefa em execução"""
    print("Executando a função concluir_tarefa")  # [Tópico 10]
    global tarefa_em_execucao
    print("\n--- 4. Concluir Tarefa ---")
 
 
    if tarefa_em_execucao is None:
        print("[INFO] Nenhuma tarefa está em execução.")
        return
 
 
    tarefa_em_execucao["Data de Conclusão"] = datetime.now()
    tarefa_em_execucao["Status"] = "Concluída"
 
 
    print(f"[SUCESSO] Tarefa '{tarefa_em_execucao['Título']}' concluída em: "
          f"{tarefa_em_execucao['Data de Conclusão'].strftime('%Y-%m-%d %H:%M:%S')}")
    tarefa_em_execucao = None
 
 
 
def excluir_concluidas_antigas():
    """Exclui tarefas concluídas há mais de uma semana"""
    print("Executando a função excluir_concluidas_antigas")  # [Tópico 10]
    global lista_de_tarefas
    print("\n--- 5. Excluir Concluídas Antigas ---")
 
 
    data_limite = datetime.now() - timedelta(weeks=1)
    tarefas_mantidas = []
    tarefas_excluidas_count = 0
 
 
    for tarefa in lista_de_tarefas:
        if tarefa["Status"] == "Concluída" and tarefa["Data de Conclusão"] and tarefa["Data de Conclusão"] < data_limite:
            tarefas_excluidas_count += 1
        else:
            tarefas_mantidas.append(tarefa)
 
 
    lista_de_tarefas = tarefas_mantidas
 
 
    if tarefas_excluidas_count > 0:
        print(f"[SUCESSO] {tarefas_excluidas_count} tarefa(s) concluída(s) antiga(s) excluída(s).")
    else:
        print("[INFO] Nenhuma tarefa concluída antiga para excluir.")
 
 
 
def exibir_relatorio():
    """Exibe relatório de todas as tarefas"""
    print("Executando a função exibir_relatorio")  # [Tópico 10]
    print("\n--- 6. Relatório de Tarefas ---")
 
 
    if not lista_de_tarefas:
        print("[INFO] A lista de tarefas está vazia.")
        return
 
 
    for tarefa in lista_de_tarefas:
        data_conc = tarefa['Data de Conclusão'].strftime('%Y-%m-%d %H:%M:%S') if tarefa['Data de Conclusão'] else "N/A"
        print(f"\nID: {tarefa['ID']}")
        print(f"  Título: {tarefa['Título']}")
        print(f"  Prioridade: {tarefa['Prioridade']}")
        print(f"  Status: {tarefa['Status']}")
        print(f"  Origem: {tarefa['Origem da Tarefa']}")
        print(f"  Data de Conclusão: {data_conc}")
 
 
 
def menu_principal():
    """Menu principal com tratamento de exceções"""
    print("Executando a função menu_principal")  # [Tópico 10]
    while True:
        print("\n\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Criar Nova Tarefa")
        print("2. Pegar Próxima Tarefa (Verificar Urgência)")
        print("3. Atualizar Prioridade de Tarefa")
        print("4. Concluir Tarefa em Execução")
        print("5. Excluir Concluídas Antigas (> 1 semana)")
        print("6. Exibir Relatório de Tarefas")
        print("7. Sair")
 
 
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números.")
            continue
 
 
        if escolha == 1:
            criar_tarefa()
        elif escolha == 2:
            verificar_e_pegar_tarefa()
        elif escolha == 3:
            atualizar_prioridade()
        elif escolha == 4:
            concluir_tarefa()
        elif escolha == 5:
            excluir_concluidas_antigas()
        elif escolha == 6:
            exibir_relatorio()
        elif escolha == 7:
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Tente novamente.")
 
 
 
# Corpo Principal
 
 
if __name__ == "__main__":
    menu_principal()