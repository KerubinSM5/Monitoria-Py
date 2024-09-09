def bubblesort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 20]
print("Lista selecionada:", lista)
lista_ordem = bubblesort(lista)
print("Lista depois da ordenação:", lista_ordem)