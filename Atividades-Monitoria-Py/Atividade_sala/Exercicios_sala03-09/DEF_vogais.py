def vogais(s):
    vog = set('aeiouAEIOU')
    contador = sum(1 for char in s if char in vog)
    return contador

s = str(input("Digite uma palavra: "))
print(f"Há {vogais(s)} vogais em {s}")