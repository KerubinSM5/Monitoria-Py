def seq_crescente():
    I = int(input("Insira o I inicial crescente: "))
    J = int(input("Insira o J inicial crescente: "))
    print("Sequencia crescente:")
    while J <= 60:
        print(f"I={I} J={J}")
        I -= 3
        J += 5

def seq_decrescente():
    I = int(input("Insira o I inicial decrescente: "))
    J = int(input("Insira o J inicial decrescente: "))
    print("Decrescente:")
    while J >= 0:
        print(f"I={I} J={J}")
        I += 3
        J -= 5

seq_crescente()
seq_decrescente()