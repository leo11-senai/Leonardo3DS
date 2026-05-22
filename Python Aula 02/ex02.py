i = 0
lista_alunos = []
nome = ''


while True:
    nome = input(f'Digite o nome do aluno {i}: ')
    
    if nome == '':
        break 
    
    
    lista_alunos.append(nome)  # função append serve para adicionar um novo item na lista
    i += 1
    
    if nome == '':
        break 


print(f'Essa é a lista de alunos: {lista_alunos}')