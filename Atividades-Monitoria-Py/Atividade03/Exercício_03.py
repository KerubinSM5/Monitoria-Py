#Exercício03

#variáveis de controle do contador
controle = 0
num_zero = 0
num_outros = 0

while True:
    num = int(input("Digite um numero (-1 para encerrar): "))
    if num == -1: #encerra o código
        break
    if num == 0: #conta o numero 0
        num_zero += 1
    else:
        num_outros += 1
#saída de dados
print(f"O numero zero foi digitado {num_zero}")