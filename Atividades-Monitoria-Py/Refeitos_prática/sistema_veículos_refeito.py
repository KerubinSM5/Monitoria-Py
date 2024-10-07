class Veiculo:
    def info(self):
        pass
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__preco = preco
    def info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preco R$: {self.__preco:.2f}"
    def set_preco(self, novo_preco):
        self.__preco = novo_preco
    def get_preco(self):
        return self.__preco

class Bicicleta(Veiculo):
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
    def info(self):
        return f"Marca: {self.marca}, Tipo: {self.tipo}"
class Garagem:
    def __init__(self):
        self.veiculos = []
    def add_veiculos(self, veiculo):
        self.veiculos.append(veiculo)
    def remove_veiculos(self,veiculo):
        self.veiculos.remove(veiculo)
    def mostra_veiculos(self):
        if not self.veiculos:
            print("Sem veiculos na garagem!")
        else:
            for veiculo in self.veiculos:
                print(veiculo.info())

if __name__ == '__main__':
    garagem = Garagem()

    carro1 = Carro("Toyota", "Corolla", 2020, 75000.00)
    carro1.set_preco(500) #altera o preço para 500
    bicicleta1 = Bicicleta("Trek", "mountain")

    garagem.add_veiculos(carro1)
    garagem.add_veiculos(bicicleta1)
    garagem.mostra_veiculos()

