x = int(input("Insira o valor de x: "))
y = int(input("Insira o valor de y: "))

Rafael = ((3 * x) ** 2) + (y ** 2)
Beto = (2 * (x ** 2)) + ((5*y) ** 2)
Carlos = (-100 * x) + (y ** 3)

if (Rafael > Beto): #Comparação de valores resultante das fórmulas
    print("Rafael ganhou")
elif (Carlos >  Beto):
    print("Carlos ganhou")
else:
    print("Beto ganhou")