segundos = int(input("insira os segundos "))

horas = segundos // 3600 #calcula as horas
minutos = (segundos % 3600) // 60 #extrai as horas para depois calcular os minutos
segundosrest = segundos % 60 #calcula o resto de segundos após extrair horas e minutos

print(horas, ":", minutos, ":", segundosrest)