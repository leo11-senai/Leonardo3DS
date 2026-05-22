while True:
    texto = input('Digite um número [s para sair]: ')
    
    if texto == 's':
        break
    
    numero = int(texto)
    
    if numero % 2 == 0:
        continue
    print(f'{numero} é impar! Seu quadrado é {numero ** 2}')
    