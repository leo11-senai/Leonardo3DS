import random
i = 0
lista = []
while i < 3:
    num = random.randint(1,6)
    print(num)
    lista.append(num)
    i += 1

soma = sum(lista)

if soma < 6:
    print(f"{soma}, Falha")
elif soma >= 6 and soma <= 12:
    print(f"{soma} Sucesso")
elif soma > 12:
    print(f"{soma} Critico")