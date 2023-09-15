import tkinter as tk

# Função para salvar os dados inseridos pelo usuário
def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    data_nascimento = entry_data_nascimento.get()

    # Aqui você pode fazer o que quiser com os dados, como imprimi-los
    print("Nome:", nome)
    print("Idade:", idade)
    print("Data de Nascimento:", data_nascimento)

# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastrinho")
janela.geometry("300x200")
janela.configure(bg="blue")  # Define o fundo da janela como azul

# Rótulo e entrada para o nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Rótulo e entrada para a idade
label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

# Rótulo e entrada para a data de nascimento
label_data_nascimento = tk.Label(janela, text="Data de Nascimento:")
label_data_nascimento.pack()
entry_data_nascimento = tk.Entry(janela)
entry_data_nascimento.pack()

# Botão para salvar os dados
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_dados)
botao_salvar.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
