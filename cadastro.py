#instale a biblioteca customtkinter para o estilo mais moderno
# pip install customtkinter
# pip install packaging

import customtkinter as ctk

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

app = ctk.CTk()  
app.geometry("1280x720")

# MENU
frame_menu = ctk.CTkFrame(app)
frame_menu.grid(row=0, column=0, padx=30, pady=(20, 0))

txt_menu = ctk.CTkLabel(frame_menu, text= "Menu", font=("Helvetica", 15))
txt_menu.grid(row = 0, column = 0, pady = 15, padx = 10)

btn_cadastro = ctk.CTkButton(frame_menu, text="Cadastro")
btn_cadastro.grid(row = 2, column = 0, pady = 15, padx = 10)

btn_listagem = ctk.CTkButton(frame_menu, text="Listagem")
btn_listagem.grid(row = 3, column = 0, pady = 15, padx = 10)    

txt_menu = ctk.CTkLabel(frame_menu, text= "Vitor Miranda", font=("Helvetica", 15))
txt_menu.grid(row = 4, column = 0, pady=(450, 20), padx = 10)

# FORMULÁRIO DO ENTREVISTADO
frame_form = ctk.CTkFrame(app)
frame_form.grid(row=0, column=1, padx=5, pady=(0, 0))

txt_title1 = ctk.CTkLabel(frame_form, text= "Dados do entrevistado", font=("Helvetica", 15))
txt_title1.grid(row = 0, column = 1, pady = 15, padx = 5)

input_nome = ctk.CTkEntry(frame_form, placeholder_text="Nome")
input_nome.grid(row = 1, column = 1, pady = 15, padx = 10)

input_telefone = ctk.CTkEntry(frame_form, placeholder_text="Nome")
input_telefone.grid(row = 2, column = 1, pady = 15, padx = 10)


tbox_bio = ctk.CTkTextbox(frame_form, 100, 100)
tbox_bio.grid(row = 3, column = 1, pady = 15, padx = 10, sticky="ew")

# NOTAS DO ENTREVISTADO

app.mainloop()