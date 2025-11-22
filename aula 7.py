print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Estoque      - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
from datetime import datetime
 
 
# Dados iniciais do estoque
estoque = [
    {
        "codigo": 101,
        "descricao": "Mouse",
        "quantidade": 50,
        "valor_unitario": 120.00,
        "data_movimentacao": "15/09/2025"
    },
    {
        "codigo": 102,
        "descricao": "Teclado",
        "quantidade": 30,
        "valor_unitario": 350.00,
        "data_movimentacao": "18/09/2025"
    },
    {
        "codigo": 103,
        "descricao": "Monitor",
        "quantidade": 15,
        "valor_unitario": 1200.00,
        "data_movimentacao": "20/09/2025"
    },
    {
        "codigo": 104,
        "descricao": "Headset",
        "quantidade": 45,
        "valor_unitario": 220.00,
        "data_movimentacao": "21/09/2025"
    },
    {
        "codigo": 105,
        "descricao": "Webcam",
        "quantidade": 60,
        "valor_unitario": 150.00,
        "data_movimentacao": "19/09/2025"
    }
]
 
 
# Função para exibir o estoque
def exibir_estoque():
    print("\n=== ESTOQUE ATUAL ===")
    for produto in estoque:
        valor_total = produto["quantidade"] * produto["valor_unitario"]
        print(f"Código: {produto['codigo']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Valor Unitário: R$ {produto['valor_unitario']:.2f}")
        print(f"Valor Total: R$ {valor_total:.2f}")
        print(f"Última Movimentação: {produto['data_movimentacao']}")
        print("-" * 40)
 
 
# Função para adicionar um novo produto
def adicionar_produto():
    codigo = int(input("Digite o código do produto: "))
    descricao = input("Digite a descrição do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    data = datetime.now().strftime("%d/%m/%Y")  # Data atual
    
    novo_produto = {
        "codigo": codigo,
        "descricao": descricao,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "data_movimentacao": data
    }
    
    estoque.append(novo_produto)
    print("\n Produto adicionado com sucesso!")
 
 
# Função para atualizar o estoque
def atualizar_estoque():
    codigo = int(input("Digite o código do produto: "))
    for produto in estoque:
        if produto["codigo"] == codigo:
            print(f"Produto encontrado: {produto['descricao']} (Qtd: {produto['quantidade']})")
            movimentacao = int(input("Digite a quantidade para movimentar (positiva = entrada, negativa = saída): "))
            
            if movimentacao < 0 and abs(movimentacao) > produto["quantidade"]:
                print("ERRO: Não há quantidade suficiente em estoque!")
            elif movimentacao == 0:
                print("⚠ Nenhuma movimentação realizada.")
            else:
                produto["quantidade"] += movimentacao
                produto["data_movimentacao"] = datetime.now().strftime("%d/%m/%Y")
                print("Movimentação realizada com sucesso!")
            return
    print("Produto não encontrado!")
 
 
# Menu principal
def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE - O ARMAZÉM DA INFORMÁTICA ===")
        print("1 - Exibir estoque")
        print("2 - Adicionar produto")
        print("3 - Atualizar estoque")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            exibir_estoque()
        elif opcao == "2":
            adicionar_produto()
        elif opcao == "3":
            atualizar_estoque()
        elif opcao == "4":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente!")
 
 
# Executar o programa
menu()