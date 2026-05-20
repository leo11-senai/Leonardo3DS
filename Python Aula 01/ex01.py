contador = 0

variavel = input('Qual é o seu nome?')
horario = input('Qual é o turno em que você está respondendo? ( Manhã / Tarde / Noite )')

while contador == contador:
    match horario:
        case 'Manhã':
            print(f'Bom dia, {variavel}!!')
        case 'Tarde':
            print(f'Boa tarde, {variavel}')
        case 'Noite':
            print(f'Boa noite, {variavel}')
        case _:
            print(f'Olá, {variavel}')



