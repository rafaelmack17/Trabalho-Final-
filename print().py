print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 1  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
mult2 = 0
mult3 = 0
 
 
for i in range(1, 31):
    print(i)
    if i % 2 == 0:
        mult2 += 1
    if i % 3 == 0:
        mult3 += 1
 
 
print("Múltiplos de 2:", mult2)
print("Múltiplos de 3:", mult3)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 2  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
for n in range(15, -1, -1):
    print(n)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 3  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
numero = 10
if numero % 2 == 0 and numero % 5 == 0:
    print("Divisível por 2 e 5")
else:
    print("Não é divisível por 2 e 5")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 4  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
soma_total = 0
for n in range(1, 51):
    soma_total += n
print("Soma total:", soma_total)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 5  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
votos_A = 0
votos_B = 0
 
 
while True:
    voto = int(input("Digite 1 para A, 2 para B ou 0 para encerrar: "))
    if voto == 0:
        break
    elif voto == 1:
        votos_A += 1
    elif voto == 2:
        votos_B += 1
 
 
if votos_A > votos_B:
    print("Vencedor: Candidato A")
elif votos_B > votos_A:
    print("Vencedor: Candidato B")
else:
    print("Empate")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 6  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
 
num = int(input("Digite um número de 1 a 10: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 7  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
senha_correta = "1234"
 
 
for tentativa in range(3):
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso Concedido")
        break
else:
    print("Acesso Bloqueado")
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 8  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
soma_pares = 0
soma_impares = 0
 
 
for n in range(1, 101):
    if n % 2 == 0:
        soma_pares += n
    else:
        soma_impares += n
 
 
print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 9  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
palavra = input("Digite uma palavra: ").lower()
vogais = 0
consoantes = 0
 
 
for letra in palavra:
    if letra in "aeiou":
        vogais += 1
    elif letra.isalpha():
        consoantes += 1
 
 
print("Vogais:", vogais)
print("Consoantes:", consoantes)
 
 
print()
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - Bloco de Codigo: Exercicio 10  - - -")
print("- - - - - - - - - - - - - - - - - - - - -")
 
 
while True:
    op = input("Digite a operação (+, -, *, /) ou 'sair': ")
    if op == "sair":
        break
 
 
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
 
 
    if op == "+":
        print("Resultado:", n1 + n2)
    elif op == "-":
        print("Resultado:", n1 - n2)
    elif op == "*":
        print("Resultado:", n1 * n2)
    elif op == "/":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro: divisão por zero!")
    else:
        print("Operação inválida")