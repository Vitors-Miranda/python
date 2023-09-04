class Pessoa(): 
    def __init__(self):
        self.nome = ''
        self.cpf = ''

class Casa():
    def __init__(self):
        self.morador = Pessoa()
        self.rua =''
        self.cidade = ''

class Fatura():
    def __init__(self, codigo):
        self.codigo = codigo
        self.usuario = Casa()

pessoa1 = Pessoa()
pessoa1.nome = "Vitor"
pessoa1.cpf = "123123123"

casa1 = Casa()
casa1.rua = "Logo ali"
casa1.cidade = "Torre de Pedra"
casa1.morador = pessoa1

fatura1 = Fatura(123123)
fatura1.usuario = casa1

print(fatura1.usuario.morador.cpf)
print(fatura1.usuario.morador.nome)
print(fatura1.usuario.rua)