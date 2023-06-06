
headers = ["Lanches", "Bebidas", "Sobremesas", "Tipo de Entrega", "Sair"]
options = ["Sandubão do bão", "Méqui Delícia"], ["Coka Koala", "Dolly"], ["Bolinho do Bom", "Torta Gostosa"], ["Delivery", "Retirada"],
valores = [[], [], [], []]


def menu():
    cont = 1
    print("\n--- Menu de produtos ---")
    for header in headers:
        print(f"{cont}. {header}")
        cont += 1
    escolha = int(input("Escolha a opção desejada: ")) -1
    print("\n")
    choices(escolha)

def choices(escolha):
    cont = 1
    try:
        for value in options [escolha]:
            print(f"{cont}. {value}")
            cont +=1
        print(f"{cont}. Voltar ao menu.")
        produto = int(input("Digite a opção: ")) -1
        if produto in [0,1]:
            valores[escolha].append(produto)
    except:
        for index in valores:
            for value in index:
                print(valores.index(index))
                print(options[valores.index(index)][value])
        exit()