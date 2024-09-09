def Divisores(n):
    if n <= 0:
        return print("O valor não pode ser igual a zero ou negativo")

    div = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n//i)

    return sorted(div)

num = int(input("Digite um valor: "))
div = Divisores(num)
print(f"Divisores de {num}: {div}")