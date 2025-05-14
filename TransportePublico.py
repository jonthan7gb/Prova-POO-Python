class Transporte():
    def __init__(self, transp, id, capacidade_passsageiros, linha_operação):
        self.transp = transp
        self.id = id
        self.capacidade_passsageiros = capacidade_passsageiros
        self.linha_operação = linha_operação

    def exibir_status(self):
        print("Transporte: ", self.transp)
        print("ID: ", self.id)
        print("Capacidade de passageiros: ", self.capacidade_passsageiros)
        print("Linha de operação: ", self.linha_operação)
        print(35 * "=")

class Onibus(Transporte):
    def __init__(self, transp, id, capacidade_passsageiros, linha_operação, tipo):
        super().__init__(transp, id, capacidade_passsageiros, linha_operação)
        self.tipo = tipo

    def exibir_status(self):
        print("Transporte: ", self.transp)
        print("ID: ", self.id)
        print("Capacidade de passageiros: ", self.capacidade_passsageiros)
        print("Linha de operação: ", self.linha_operação)
        print("Tipo: ", self.tipo)
        print(35 * "=")

class Trem(Transporte):
    def __init__(self, transp, id, capacidade_passsageiros, linha_operação, numero_vagoes):
        super().__init__(transp, id, capacidade_passsageiros, linha_operação)
        self.numero_vagoes = numero_vagoes

    def exibir_status(self):
        print("Transporte: ", self.transp)
        print("ID: ", self.id)
        print("Capacidade de passageiros: ", self.capacidade_passsageiros)
        print("Linha de operação: ", self.linha_operação)
        print("Número de vagões: ", self.numero_vagoes)
        print(35 * "=")


class Metro(Transporte):
    def __init__(self, transp, id, capacidade_passsageiros, linha_operação, subterraneo):
        super().__init__(transp, id, capacidade_passsageiros, linha_operação)
        self.subterraneo = subterraneo
    
    def exibir_status(self):
        print("Transporte: ", self.transp)
        print("ID: ", self.id)
        print("Capacidade de passageiros: ", self.capacidade_passsageiros)
        print("Linha de operação: ", self.linha_operação)
        print("É subterrâneo?: ", self.subterraneo)
        print(35 * "=")


def mostrarMenu():
    print("==== Transporte Público ====")
    print("1 - Cadastrar Transporte")
    print("2 - Listar Transportes")
    print("3 - Remover Transporte")
    print("4 - Sair do sistema")

