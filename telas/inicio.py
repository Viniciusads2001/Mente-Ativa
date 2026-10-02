import customtkinter as ctk
from tkinter import messagebox

class TelaInicial:

    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.janela = ctk.CTk()

        self.janela.title("Mente Ativa")
        self.janela.geometry("1000x700")

        cabecalho = ctk.CTkFrame(self.janela, height=90)
        cabecalho.pack(fill="x") 

        titulo = ctk.CTkLabel(
            cabecalho,
            text= "Mente Ativa",
            font=("Arial", 40, "bold")
        )
        titulo.pack()

        nome = ctk.CTkLabel(
            cabecalho,
            text="Profissional Responsável",
            font=("Arial", 30, "bold")
        )
        nome.pack()

        profissao = ctk.CTkLabel(
            cabecalho,
            text="Neuropsicopedagoga e Psicopedagoga Clínica e Institucional",
            font=("Arial", 18, "bold")
        )
        profissao.pack()


        corpo = ctk.CTkFrame(self.janela)
        corpo.pack(fill="both",expand=True)

        menu = ctk.CTkFrame(corpo)
        menu.pack(side="left", fill="y")

        botao_inicio = ctk.CTkButton( menu, text="Início", command=self.mostrar_inicio)
        botao_inicio.pack(fill="x", padx=10, pady=5)


        botao_pacientes = ctk.CTkButton( menu, text="Pacientes", command=self.mostrar_pacientes )
        botao_pacientes.pack()

        botao_agenda = ctk.CTkButton( menu, text="Agenda", command=self.mostrar_agenda )
        botao_agenda.pack()

        botao_atendimentos = ctk.CTkButton(menu, text="Atendimentos", command=self.mostrar_atendimentos )
        botao_atendimentos.pack()

        botao_mostrar_evolucao = ctk.CTkButton(menu, text="Evolução", command=self.mostrar_evolucao)
        botao_mostrar_evolucao.pack()

        botao_avaliacoes = ctk.CTkButton(menu, text="Avaliações", command=self.mostrar_avaliacoes)
        botao_avaliacoes.pack()

        botao_relatorios = ctk.CTkButton(menu, text="Relatórios", command=self.mostrar_relatorios)
        botao_relatorios.pack()

        botao_documentos = ctk.CTkButton(menu, text="Documentos",command=self.mostrar_documentos)
        botao_documentos.pack()

        botao_configuracoes = ctk.CTkButton(menu, text="Configurações", command=self.mostrar_configurações)
        botao_configuracoes.pack()

        self.conteudo = ctk.CTkFrame(corpo)
        self.conteudo.pack(side="left", fill="both", expand=True)

        rodape = ctk.CTkFrame(self.janela, height=90)
        rodape.pack(side="bottom",fill="x")

        self.pacientes = []
        self.proximo_id = 1
        self.paciente_editando = None

    def mostrar_inicio(self):

        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto = ctk.CTkLabel(
            self.conteudo,
            text="Mente Ativa"
        )
        
        texto.pack()

        card_pacientes = ctk.CTkFrame(
            self.conteudo,
            width=200,
            height=120
        )

        pacientes = ctk.CTkLabel(
            card_pacientes,
            text = "Pacientes",
            font=("Arial", 18,"bold")
        )
        pacientes.pack()
            
        quantidade = ctk.CTkLabel(
            card_pacientes,
            text=str(len(self.pacientes))
        )

        quantidade.pack()

        card_pacientes.pack(
            side="left",
            padx=20,
            pady=20
        )

        card_atendimentos = ctk.CTkFrame(
            self.conteudo,
            width=200,
            height=120
        )
        
        card_atendimentos.pack(
            side= "left",
            padx=20,
            pady=20
        )

        atendimentos = ctk.CTkLabel(
            card_atendimentos,
            text= "Atendimentos",
            font=("Arial", 18, "bold")
        )

        atendimentos.pack()

        card_quantidade_atendimento = ctk.CTkLabel(
            card_atendimentos,
            text = "12", 
            font=("Arial", 30,"bold")
        )      

        card_quantidade_atendimento.pack()

    def mostrar_novo_paciente(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        novo_paciente = ctk.CTkLabel(
            self.conteudo,
            text="Novo Paciente",
            font=("Arial", 28, "bold")
        )
        novo_paciente.pack()

        nome_completo = ctk.CTkLabel(
            self.conteudo,
            text="Nome Completo",
            font=("Arial", 28, "bold"),
        )
        nome_completo.pack()
        
        self.caixa_do_nome = ctk.CTkEntry(self.conteudo)
        self.caixa_do_nome.pack(padx=100, pady=10)   

        if self.paciente_editando is not None:
            self.caixa_do_nome.insert(
            0,
            self.paciente_editando["nome"]
            )
      
        data_nascimento = ctk.CTkLabel(
            self.conteudo,
            text="Data de Nascimento",
            font=("Arial", 30, "bold")
        )
        data_nascimento.pack()

        self.caixa_data_nascimento = ctk.CTkEntry(self.conteudo)
        self.caixa_data_nascimento.pack(padx=100, pady=10)

        if self.paciente_editando is not None:
            self.caixa_data_nascimento.insert(
                0,
                self.paciente_editando["data_nascimento"]
            )

        nome_da_mae = ctk.CTkLabel(
            self.conteudo,
            text="Nome da Mãe",
            font=("Arial", 28,"bold")
        )
        nome_da_mae.pack()

        self.caixa_nome_mae = ctk.CTkEntry(self.conteudo)
        self.caixa_nome_mae.pack(padx=200,pady=10)

        if self.paciente_editando is not None:
            self.caixa_nome_mae.insert(
                0,
                self.paciente_editando["nome_mae"]
            )

        telefone = ctk.CTkLabel(
            self.conteudo,
            text="Telefone",
            font=("Arial", 28, "bold")
        )

        telefone.pack()
    

        self.caixa_telefone = ctk.CTkEntry(self.conteudo)
        self.caixa_telefone.pack(padx=200, pady=10)

        if self.paciente_editando is not None:
            self.caixa_telefone.insert(
                0,
                self.paciente_editando["telefone"]
            )

        botao_continuar = ctk.CTkButton(
            self.conteudo,
            text="Continuar",
            command=self.salvar_paciente
        )

        botao_continuar.pack()  

        self.mensagem_erro = ctk.CTkLabel(
            self.conteudo,
            text=""
        )
        self.mensagem_erro.pack()
    
    def salvar_paciente(self):
        
        self.nome_do_paciente = self.caixa_do_nome.get()

        if self.nome_do_paciente=="":
            self.mensagem_erro.configure(
                 text="Digite o Nome do Paciente!"
            )           
            return
        
        self.data_nascimento = self.caixa_data_nascimento.get()

        if self.data_nascimento=="":
            self.mensagem_erro.configure(
                 text="Digite a Data de Nascimento do Paciente"
            )
            return
        
        self.nome_mae = self.caixa_nome_mae.get()

        if self.nome_mae=="":
            self.mensagem_erro.configure(
                 text="Digite o Nome da Mãe do Paciente!"
            )
            return
        
        self.telefone_paciente = self.caixa_telefone.get()

        if self.telefone_paciente=="":
            self.mensagem_erro.configure(
                 text="Digite o telefone Paciente!"
            )
            return

        self.mensagem_erro.configure(text="")

        paciente = {
            "nome": self.nome_do_paciente,
            "data_nascimento": self.data_nascimento,
            "nome_mae": self.nome_mae,
            "telefone": self.telefone_paciente
        }

        if self.paciente_editando is not None:

            paciente["id"] = self.paciente_editando["id"]

            self.paciente_editando.update(paciente)

            self.paciente_editando = None

        else:

            paciente["id"] = self.proximo_id

            self.pacientes.append(paciente)

            self.proximo_id += 1

        self.mostrar_confirmacao()
        
    def mostrar_pacientes(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        
        titulo = ctk.CTkLabel(
            self.conteudo,
            text="Pacientes",
            font=("Arial", 28, "bold")
        )
        titulo.pack()

        novo_paciente = ctk.CTkButton(
            self.conteudo,
            text="Novo Paciente",
            command=self.mostrar_novo_paciente
        )
        novo_paciente.pack(padx=20, pady=10)

        self.caixa_pesquisa = ctk.CTkEntry(
            self.conteudo,
            placeholder_text="Digite o Nome do Paciente"
        )
        self.caixa_pesquisa.pack(padx=20, pady=10)

        botao_pesquisar = ctk.CTkButton(
            self.conteudo,
            text="Pesquisar",
            command= self.pesquisar_pacientes
        )
        botao_pesquisar.pack()

        for paciente in self.pacientes:
            card = ctk.CTkFrame(self.conteudo)
            card.pack(
                fill="x",
                padx=20,
                pady=10
            )
            nome = ctk.CTkLabel(
                card,
                text=paciente["nome"],
                font=("Arial", 18)
            )

            nome.grid(row=0, column=0)

            data = ctk.CTkLabel(
                card,
                text="Nascimento: " + paciente["data_nascimento"]
            )

            data.grid(row=1, column=0)

            mae = ctk.CTkLabel(
                card,
                text="Mãe: " + paciente["nome_mae"]
            )

            mae.grid(row=2, column=0)

            telefone = ctk.CTkLabel(
                card,
                text="Telefone: " + paciente["telefone"]
            )

            telefone.grid(row=3,column=0)

            botao_editar =ctk.CTkButton(
                card,
                text="Editar",
                command=lambda p=paciente: self.editar_paciente(p)
            )
            botao_editar.grid(row=4, column=0)

            botao_excluir = ctk.CTkButton(
                card,
                text="Excluir",
                command=lambda p=paciente: self.excluir_paciente(p)
            )

            botao_excluir.grid(row=4, column= 3)

            botao_ficha = ctk.CTkButton(
                card,
                text="Ver Ficha",
                command=lambda p=paciente: self.mostrar_ficha_paciente(p)
            )

            botao_ficha.grid(row=4, column=4)

    def pesquisar_pacientes(self):
        busca = self.caixa_pesquisa.get()
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        for paciente in self.pacientes:
            if paciente['nome'] == busca:
                self.mostrar_ficha_paciente(paciente)
                break

    def excluir_paciente(self,paciente):
       
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja Excluir o paciente {paciente['nome']} ? "
        )
        
        if resposta == True:
            self.pacientes.remove(paciente)
            self.mostrar_pacientes()

    def mostrar_ficha_paciente(self,paciente):

        for widget in self.conteudo.winfo_children():
            widget.destroy()

        card = ctk.CTkFrame(self.conteudo)
        card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        nome = ctk.CTkLabel(
            card,
            text=f"Nome: {paciente['nome']}"
        )
        nome.grid(row=0, column=0)

        data_nascimento = ctk.CTkLabel(
            card,
            text=f"Data de Nascimento: {paciente['data_nascimento']} "
        )
        data_nascimento.grid(row=1, column=0)

        nome_mae = ctk.CTkLabel(
            card,
            text=f"Nome da Mãe: {paciente['nome_mae']}"
        )
        nome_mae.grid(row=2, column=0)

        telefone = ctk.CTkLabel(
            card,
            text=f"Telefone: {paciente['telefone']}"
        )
        telefone.grid(row=3, column=0)

        botao_editar = ctk.CTkButton(
            card,
            text="Editar",
            command=lambda p=paciente: self.editar_paciente(p)
        )
        botao_editar.grid(row=4, column=0)

        botao_excluir = ctk.CTkButton(
            card,
            text="Excluir",
            command=lambda p=paciente: self.excluir_paciente(p)
        )

        botao_excluir.grid(row=4, column=1)

        botao_voltar = ctk.CTkButton(
            card,
            text="Voltar para Pacientes",
            command=self.mostrar_pacientes
        )

        botao_voltar.grid(row=4, column=2)

    def mostrar_confirmacao(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto = ctk.CTkLabel(
            self.conteudo,
            text="Nome Cadastrado"
        )
        texto.pack()

        nome = ctk.CTkLabel(
            self.conteudo,
            text=self.nome_do_paciente
        )
        nome.pack()     

        botao = ctk.CTkButton(
            self.conteudo,
            text="Voltar para Pacientes",
            command=self.mostrar_pacientes
        )

        botao.pack()

        editar = ctk.CTkButton(
            self.conteudo,
            text= "Editar",
            command=lambda: self.editar_paciente(self.pacientes[-1])
        )
        editar.pack()

    def editar_paciente(self,paciente):
        self.paciente_editando = paciente
        self.mostrar_novo_paciente()

    def mostrar_agenda(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto = ctk.CTkLabel(
            self.conteudo,
            text="Agenda"
        )

        texto.pack()

    def mostrar_atendimentos(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto = ctk.CTkLabel(
            self.conteudo,
            text="Atendimentos"
        )
        texto.pack()

    def mostrar_evolucao(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto = ctk.CTkLabel(
            self.conteudo,
            text="Evolução"
        )
        texto.pack()

    def mostrar_avaliacoes(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto = ctk.CTkLabel(
            self.conteudo,
            text="Avaliações"
        )

        texto.pack()

    def mostrar_relatorios(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto= ctk.CTkLabel(
            self.conteudo,
            text="Relatórios"
        )

        texto.pack()

    def mostrar_documentos(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto= ctk.CTkLabel(
            self.conteudo,
            text="Documentos"
        )

        texto.pack()

    def mostrar_configurações(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

        texto= ctk.CTkLabel(
            self.conteudo,
            text="Configurações"
        )

        texto.pack()

    def iniciar(self):
        self.janela.mainloop()
        