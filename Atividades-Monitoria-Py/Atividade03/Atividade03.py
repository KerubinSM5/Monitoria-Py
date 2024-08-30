'''#Atividade01
num_pos = 0
num_neg = 0
num_zero = 0
controle = 0

while True:
    num = int(input("Digite um numero (-1 para terminar): "))
    if num == -1:
        break
    if num < 0:
        num_neg += 1
    elif num > 0:
        num_pos +=1
    else:
        num_zero += 1
    controle += 1

print(f"{num_pos} números positivos")
print(f"{num_neg} números negativos")
print(f"{num_zero} zero")
'''
'''#Exercício02
controle = 0
num_c1 = 0
num_c2 = 0
num_c3 = 0
num_div1 = int(input("Digite um primeiro numero divisor: "))
num_div2 = int(input("Digite um segundo numero divisor: "))
num_div3 = int(input("Digite um terceiro numero divisor: "))

while True:
    num = int(input("Digite seu numero (-1 para encerrar): "))
    if num == -1:
        break

    if num % num_div1 == 0:
        print(f"{num} + a")
        num_c1 += 1
    if num % num_div2 == 0:
        print(f"{num} + b")
        num_c2 += 1
    if num % num_div3 == 0:
        print(f"{num} + c")
        num_c3 += 1
    controle += 1

print(f"{num_c1} numeros divisiveis por {num_div1}")
print(f"{num_c2} numeros divisiveis por {num_div2}")
print(f"{num_c3} numeros divisiveis por {num_div3}")'''
#Exercício03
controle = 0
num_zero = 0
num_outros = 0

while True:
    num = int(input("Digite um numero (-1 para encerrar): "))
    if num == -1:
        break
    if num == 0:
        num_zero += 1
    else:
        num_outros += 1

print(f"O numero zero foi digitado {num_zero}")