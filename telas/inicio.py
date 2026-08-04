import customtkinter as ctk

class TelaInicial:

    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.janela = ctk.CTk()

        self.janela.title("Mente Ativa")
        self.janela.geometry("1000x700")

        titulo = ctk.CTkLabel(
            self.janela,
            text="Sistema de Gestão - Mente Ativa",
            font=("Arial", 28, "bold")
        )

        titulo.pack(pady=30)

    def iniciar(self):
        self.janela.mainloop()