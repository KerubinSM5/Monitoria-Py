def fatorial(n):
    if n  < 0:
        print("não há como definir fatorial com numeros negativos")
    contagem = 1
    for i in range(2, n+1):
            contagem *= i
    return contagem

n = int(input("Digite um numero: "))
print(fatorial(n))