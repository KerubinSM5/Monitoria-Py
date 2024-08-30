#Atividade01

#Variáveis de controle: contam os valores inseridos  
num_pos = 0
num_neg = 0
num_zero = 0
controle = 0

#Contador de valores: conta e registra os valores conforme a regra
while True:
    num = int(input("Digite um numero (-1 para terminar): ")) #entrada de valores
    if num == -1: #Quebra a repetição quando o -1 for digitado
        break
    if num < 0: #Adiciona um numero positivo na contagem caso ele seja negativo (exceto -1)
        num_neg += 1
    elif num > 0: #Adiciona um numero positivo na contagem caso ele seja positivo
        num_pos +=1
    else: #Conta os valores zero
        num_zero += 1
    controle += 1

#Saída de dados
print(f"{num_pos} números positivos")
print(f"{num_neg} números negativos")
print(f"{num_zero} zero")