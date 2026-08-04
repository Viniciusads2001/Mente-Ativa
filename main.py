import customtkinter as ctk

# Aparência
ctk.set_appearance_mode("light")  # light ou dark
ctk.set_default_color_theme("blue")

# Criando a janela
janela = ctk.CTk()

janela.title("Sistema de Pacientes")
janela.geometry("900x600")

# Título
titulo = ctk.CTkLabel(
    janela,
    text="Sistema de Cadastro de Pacientes",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=30)

# Botão
botao = ctk.CTkButton(
    janela,
    text="Novo Cadastro"
)

botao.pack()

janela.mainloop()