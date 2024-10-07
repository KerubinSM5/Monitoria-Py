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
        return f"carro: Marca - {self.marca} Modelo - {self.modelo} Ano - {self.ano} Preço - {self.__preco:.2f}"
    def set_preco(self, novo_preco):
        self.__preco = novo_preco
    def get_preco(self):
        return self.__preco

class Bicicleta(Veiculo):
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
    def info(self):
        return f"Bicicleta - {self.marca} Tipo - {self.tipo}"

class Garagem:
    def __init__(self):
        self.veiculos = []
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
    def infos(self):
        for veiculo in self.veiculos:
            print(veiculo.info())

garagem = Garagem()
carro1 = Carro("Hyundai", "N Vision 74", "2024", 1000000)
carro1.set_preco(20) #altera o preço antes privado
bicicleta1 = Bicicleta("veic", "Mountain")


garagem.adicionar_veiculo(carro1)
garagem.adicionar_veiculo(bicicleta1)
garagem.infos()
