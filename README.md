# Mente Ativa

Aplicativo desktop para gestão de pacientes de clínica, desenvolvido em Python com CustomTkinter. Projeto pessoal em desenvolvimento, focado em praticar lógica de programação, orientação a objetos e organização de código em módulos.

## Funcionalidades

- Cadastro de pacientes com validação de campos (nome, data de nascimento, nome da mãe, telefone)
- Lista de pacientes com ficha individual
- Pesquisa de paciente por nome
- Edição e exclusão de pacientes (com confirmação)
- Navegação entre telas: Início, Pacientes, Agenda, Atendimentos, Evolução, Avaliações, Relatórios, Documentos e Configurações
- Painel inicial com resumo (quantidade de pacientes e atendimentos)

## Tecnologias

- Python 3.14
- CustomTkinter (interface gráfica)
- Tkinter messagebox (diálogos de confirmação)

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Estrutura

```
SistemaPacientes/
├── main.py            # ponto de entrada
└── telas/
    └── inicio.py      # janela principal e telas do sistema
```

## Roadmap

- [ ] Persistência de dados em banco SQL (em vez de armazenamento em memória)
- [ ] Implementar módulos de Agenda, Atendimentos, Evolução e Avaliações
- [ ] Relatórios e exportação de dados
