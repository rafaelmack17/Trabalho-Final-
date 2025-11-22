# ============================================================
# Funções utilitárias para arquivos
# ============================================================

def verificar_arquivos():
    """
    Verifica se os arquivos JSON necessários existem no diretório.
    Caso não existam, cria automaticamente com listas vazias.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    if not os.path.exists("tarefas.json"):
        with open("tarefas.json", "w") as f:
            json.dump([], f, indent=4)

    if not os.path.exists("tarefas_arquivadas.json"):
        with open("tarefas_arquivadas.json", "w") as f:
            json.dump([], f, indent=4)


def carregar_tarefas():
    """
    Lê o arquivo tarefas.json e retorna a lista de tarefas.

    Parâmetros: nenhum
    Retorno:
        list: lista de tarefas carregadas do arquivo
    """
    with open("tarefas.json", "r") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no arquivo tarefas.json.

    Parâmetros:
        tarefas (list): lista atualizada de tarefas a ser gravada
    Retorno: nenhum
    """
    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f, indent=4)


def salvar_arquivadas(tarefas):
    """
    Recebe uma lista de tarefas que devem ser arquivadas
    e adiciona ao arquivo tarefas_arquivadas.json.

    Parâmetros:
        tarefas (list): lista de tarefas a arquivar
    Retorno: nenhum
    """
    with open("tarefas_arquivadas.json", "r") as f:
        dados_existentes = json.load(f)

    dados_existentes.extend(tarefas)

    with open("tarefas_arquivadas.json", "w") as f:
        json.dump(dados_existentes, f, indent=4)


# Lista global principal
tarefas = []


# ============================================================
# Função: Criar tarefa
# ============================================================

def criar_tarefa():
    """
    Cria uma nova tarefa solicitando informações ao usuário,
    valida os dados e adiciona a nova tarefa à lista global.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição da tarefa: ").strip()

    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "criada_em": datetime.now().strftime("%Y-%m-%d"),
        "concluida": False,
        "arquivo": False
    }

    tarefas.append(nova_tarefa)
    print("\nTarefa criada com sucesso!\n")


# ============================================================
# Função: Listar tarefas
# ============================================================

def listar_tarefas():
    """
    Exibe todas as tarefas ativas com seus índices.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\n--- TAREFAS ATIVAS ---")
    for i, t in enumerate(tarefas):
        status = "Concluída" if t["concluida"] else "Pendente"
        print(f"{i} - {t['titulo']} ({status})")
    print()


# ============================================================
# Função: Concluir tarefa
# ============================================================

def concluir_tarefa():
    """
    Solicita ao usuário o índice da tarefa e marca como concluída.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    listar_tarefas()
    try:
        indice = int(input("Informe o índice da tarefa a concluir: "))
        tarefas[indice]["concluida"] = True
        print("\nTarefa marcada como concluída!\n")
    except:
        print("\nÍndice inválido!\n")


# ============================================================
# Função: Arquivar tarefas concluídas há mais de 7 dias
# ============================================================

def arquivar_tarefas_antigas():
    """
    Identifica tarefas concluídas há mais de 7 dias,
    move para o arquivo tarefas_arquivadas.json
    e remove da lista ativa.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    hoje = datetime.now()
    uma_semana = timedelta(days=7)

    para_arquivar = []

    for t in tarefas:
        if t["concluida"]:
            data = datetime.strptime(t["criada_em"], "%Y-%m-%d")
            if hoje - data > uma_semana:
                para_arquivar.append(t)

    if para_arquivar:
        salvar_arquivadas(para_arquivar)

    # Remove da lista principal
    for t in para_arquivar:
        tarefas.remove(t)


# ============================================================
# Função: Sair do sistema
# ============================================================

def sair():
    """
    Realiza o salvamento de todas as tarefas no arquivo JSON,
    executa limpeza e arquivamento automático e finaliza o sistema.

    Parâmetros: nenhum
    Retorno: nenhum (o programa encerra)
    """
    arquivar_tarefas_antigas()
    salvar_tarefas(tarefas)
    print("\nDados salvos com sucesso. Encerrando o programa...\n")
    exit()


# ============================================================
# Menu principal
# ============================================================

def menu():
    """
    Exibe o menu principal do sistema e controla as opções escolhidas
    pelo usuário até que a opção de saída seja selecionada.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    while True:
        print("""
===== MENU DO GERENCIADOR DE TAREFAS =====
1 - Criar nova tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            sair()
        else:
            print("\nOpção inválida!\n")


# ============================================================
# Inicialização do programa
# ============================================================

verificar_arquivos()
tarefas = carregar_tarefas()
menu()