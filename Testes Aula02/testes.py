def sacar(saldo,valor):
    '''
    sacar(saldo,valor): Saca dinheiro da conta 
    saldo: Valor atual da conta
    valor: Valor a ser sacado
    return: Retorna True se 
    '''

    if valor <= 0 :
        raise ValueError("Valor inválido")
    if valor > saldo: 
        raise ValueError("Saldo insuficiente")
    
    return saldo - valor