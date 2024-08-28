idade = int(input("Digite sua idade: "))

if (idade < 13):
    print("Criança")
elif (idade >= 13 and idade <= 19):
    print("Adolescente")
elif (idade >= 20 and idade <= 59):
    print("Adulto")
else:
    print("Idoso")