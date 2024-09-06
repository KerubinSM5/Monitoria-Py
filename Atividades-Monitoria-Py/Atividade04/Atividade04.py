#Descrição: Escreva um programa que some todos os números de 1 a 10.
soma = 0
for c in range(1, 11):
   soma = soma + c
print(f"soma de 1 a 10: {soma}")

#Descrição: Escreva um programa que exiba a tabuada do número 5.
for c in range(1, 11):
   print(f"5 x {c} = {c * 5}")

#Descrição: Escreva um programa que exiba todos os números pares de 1 a 20.
for x in range(2,22, 2):
    print(x)

#Descrição: Escreva um programa que exiba uma contagem regressiva de 10 a 1.
for x in range(10, 0, -1):
    print(x)

#Descrição: Escreva um programa que calcule a soma dos quadrados dos números de 1 a 5.
soma_q = 0
for q  in range(1, 6):
    soma_q += q **2
print(f"Soma: {soma_q}")

#Descrição: Escreva um programa que calcule o produto de todos os números de 1 a 10.
soma_p = 1
for sp in range(1, 11):
    soma_p *= sp
print(f"Soma dos produtos: {soma_p}")

#Escreva um programa que calcule o fatorial de um número dado pelo usuário.
soma = 1
numero = int(input("Digite um numero: "))

for fatorial in range(1, numero + 1):
    soma *= fatorial
print(soma)

#Escreva um programa que some todos os números pares entre dois números dados pelo usuário.
soma = 0
n1 = int(input("Digite um primeiro numero: "))
n2 = int(input("Digite um segundo numero: "))
for pares in range(n1, n2 + 1, 2):
    soma += pares
print(soma)

#Escreva um programa que exiba os primeiros 10 números da sequência de Fibonacci.
a = 0
b = 1
seq = []
n = 15 #define o numero de termos
for soma in range(n):
    seq.append(a)
    a, b = b, a + b
print(seq)