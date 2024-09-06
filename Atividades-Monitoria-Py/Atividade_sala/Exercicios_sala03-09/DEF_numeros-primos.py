def nprimos (n):
    if n <= 1: #1 e menores que ele não são primos
        print("Numero 1 ou menores que ele não são primos")
        return False
    for i in range(2, int(n**0.5)+1): #"identifica" se é divisivel por 2 ou raízes quadradas do numero selecionado
        if n % i == 0: #verifica se n é divisível por outro numero sem que haja resto
            print("Não é primo")
            return False
    return (f"{n} é primo")

print(nprimos(243))