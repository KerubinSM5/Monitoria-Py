#Exercício02

#Variáveis de controle: contam os valores inseridos
controle = 0
num_c1 = 0
num_c2 = 0
num_c3 = 0
#Entrada os valores que dividirão os numeros inseridos
num_div1 = int(input("Digite um primeiro numero divisor: "))
num_div2 = int(input("Digite um segundo numero divisor: "))
num_div3 = int(input("Digite um terceiro numero divisor: "))

#Contador de valores: conta e registra os valores conforme a regra
while True:
    num = int(input("Digite seu numero (-1 para encerrar): "))
    if num == -1:
        break
#Cadeia de if's: selecionam os numeros que se encaixam na regra, um unico valor entra nos 3 if's
    if num % num_div1 == 0:
        print(f"{num}")
        num_c1 += 1
    if num % num_div2 == 0:
        print(f"{num}")
        num_c2 += 1
    if num % num_div3 == 0:
        print(f"{num}")
        num_c3 += 1
    controle += 1 #contador de controle

#saída de dados
print(f"{num_c1} numeros divisiveis por {num_div1}")
print(f"{num_c2} numeros divisiveis por {num_div2}")
print(f"{num_c3} numeros divisiveis por {num_div3}")