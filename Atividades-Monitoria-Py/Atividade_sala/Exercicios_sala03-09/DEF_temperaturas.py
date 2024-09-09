def converter_temp(c):
    f = (1.8) * c + 32
    k = c + 273.15
    return f,k

temp_c = float(input("Digite a temperatura em Celsius: "))
f,k = converter_temp(temp_c)

print(f"Temperatura em Fahrenheit: {f:.2f} ºF")
print(f"temperatura em Kelvin: {k:2f} K")
