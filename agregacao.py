class Cliente():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta():
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo    
        self.limite = limite

cliente01 = Cliente('vitor', 'miranda', '489192032')
minha_conta = Conta('123-4', cliente01, 99.0, 100.0)

print(minha_conta.cliente.cpf)