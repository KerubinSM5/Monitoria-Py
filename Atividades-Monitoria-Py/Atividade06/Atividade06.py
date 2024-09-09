'''def crescente(inicio, fim, passo):
    inicio = int(input("Insira o primeiro numero: "))
    fim = int(input("Insira o numero limite: "))
    passo = int(input("Insira o passo de crescente: "))
    for crescente in range(inicio, fim, passo):
        print(crescente)'''

'''def decrescente(inicioD, fimD, passoD):
    for decrescente in range(inicioD, fimD, -passoD):
        print(decrescente)
        #print("J: ", decrescente)'''

inicio_crescente = int(input("Insira o numero inicial crescente: "))
fim_crescente = int(input("Insira o numero final crescente: "))
passo_crescente = int(input("Insira o passo de crescente: "))
for crescente in range(inicio_crescente, fim_crescente, passo_crescente):
    print("Crescentes: ", crescente)

#sequencia_crescente = crescente(inicio_crescente, fim_crescente, passo_crescente)
#print(crescente)

inicio_decrescente = int(input("Insira o numero inicial decrescente: "))
fim_decrescente = int(input("Insira o numero final decrescente: "))
passo_decrescente = int(input("Insira o passo de decrescente: "))
for decrescente in range(inicio_decrescente, fim_decrescente, passo_decrescente):
    print("Decrescente:", decrescente)

#sequencia_decrescente = decrescente(inicio_decrescente, fim_decrescente, passo_decrescente)
#print(f"Crescentes: ", sequencia_crescente)
#print(f"Decrescentes: {sequencia_decrescente}")