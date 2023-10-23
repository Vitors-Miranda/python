import tkinter as tk
def exibir_mensagem():
    label.config(text="Ola, mundo")
    print(texto1.get())

def abrir_janela():
    janela2 = tk.Toplevel()
    botao_voltar = tk.Button(janela2, text="Fechar janela", command=janela2.destroy)
    botao_voltar.pack(pady=10)

    
janela = tk.Tk()

janela.geometry("600x600")
label = tk.Label(janela, text= "Hello World!")
label.pack(pady=10)

botao1 = tk.Button(janela, text="Clique-me", command=exibir_mensagem)
botao1.pack(pady=20)

texto1 = tk.Entry(janela)
texto1.pack(pady=30)

botao2 = tk.Button(janela, text="Ir para nova janela", command=abrir_janela)
botao2.pack(pady=50)

janela.mainloop()