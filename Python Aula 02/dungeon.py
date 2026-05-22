import random as r
itens = ['Espada', 'Escudo', 'Cajado', 'Mapa', 'Armadura', 'tesouro', 'nada', 'é um mímico', 'poção duvidosa']

r.shuffle(itens)
num = int(input('Escolha um número 1 - 10: '))
num -= 1
print (itens[num])