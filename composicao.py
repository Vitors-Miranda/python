class Historico():
    def __init__(self):
        self.data_abertura = ""
        self.transacoes = []

class Conta():
    def __init__(self):
        self.cliente = ""
        self.historico = Historico()

minha_conta = Conta()
minha_conta.cliente = 'rafael'
minha_conta.historico.transacoes = [1,2,3,4]
minha_conta.historico.data_abertura = '04/06/2023'

print(minha_conta.historico.transacoes)