import tkinter as tk


# Criando a janela principal da aplicação
janela = tk.Tk()
janela.title("Contador de pontos")


# funções
def pontuacao():
    valor_atual = pontos.get()
    pontos.set(valor_atual + 1)



# Variáveis
pontos = tk.IntVar()
pontos.set(0)


#Adicionar Complementos à janela
# Texto
label = tk.Label(janela, textvariable= pontos)
label.pack()

# Botão
button = tk.Button(janela, text= "Clique Aqui", command=pontuacao)
button.pack()

#executar o loop de eventos principal da aplicação
janela.mainloop()
