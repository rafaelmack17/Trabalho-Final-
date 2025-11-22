# Exercício 1
# Crie uma variável nome com seu nome, uma variável idade com sua idade 
# e uma variável altura com sua altura. 
# Imprima uma frase que use todas as variáveis.
# ============================================================

# Passos do algoritmo:
# 1. Criar três variáveis: nome, idade e altura.
# 2. Montar uma frase usando f-string.
# 3. Imprimir a frase.

nome = "Seu Nome"
idade = 25
altura = 1.75

print(f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros.")


# ============================================================
# Exercício 2
# Crie duas variáveis numero1 = 10 e numero2 = 5.
# Imprima a soma, subtração, multiplicação e divisão entre elas.
# ============================================================

# Passos do algoritmo:
# 1. Criar as variáveis numero1 e numero2.
# 2. Calcular cada operação.
# 3. Imprimir os resultados.

numero1 = 10
numero2 = 5

print("Soma:", numero1 + numero2)
print("Subtração:", numero1 - numero2)
print("Multiplicação:", numero1 * numero2)
print("Divisão:", numero1 / numero2)


# ============================================================
# Exercício 3
# Crie uma variável peso e uma variável altura.
# Calcule o IMC (peso / altura²) e imprima o resultado.
# ============================================================

# Passos do algoritmo:
# 1. Criar variáveis para peso e altura.
# 2. Calcular o IMC usando a fórmula.
# 3. Imprimir o valor calculado.

peso = 70
altura = 1.75

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)


# ============================================================
# Exercício 4
# Crie uma variável total_compra = 150 e desconto = 20.
# Calcule o valor final da compra após o desconto e imprima o resultado.
# ============================================================

# Passos do algoritmo:
# 1. Criar as variáveis total_compra e desconto.
# 2. Subtrair o desconto do total.
# 3. Imprimir o valor final.

total_compra = 150
desconto = 20

valor_final = total_compra - desconto

print("Valor final após desconto:", valor_final)


# ============================================================
# Exercício 5
# Crie uma variável numero_inteiro e verifique se ele é par ou ímpar usando %.
# Imprima a resposta.
# ============================================================

# Passos do algoritmo:
# 1. Criar a variável numero_inteiro.
# 2. Usar o operador % para verificar o resto da divisão por 2.
# 3. Imprimir se é par ou ímpar.

numero_inteiro = 7

if numero_inteiro % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")