print("Fila atual:", fila)
 
 
# Removendo o primeiro elemento (sair da fila)
primeiro = fila.pop(0)
print("Elemento atendido:", primeiro)
 
 
print("Fila após atendimento:", fila)

pilha = []
# Adicionando elementos (empilhar)
pilha.append("A")
pilha.append("B")
pilha.append("C")
 
 
print("Pilha atual:", pilha)
 
 
# Removendo o último elemento (desempilhar)
elemento_removido = pilha.pop()
print("Elemento removido:", elemento_removido)
 
 
print("Pilha após remoção:", pilha)
 
 
# Verificando o elemento do topo (sem remover)
topo = pilha[-1]
print("Topo da pilha:", topo)