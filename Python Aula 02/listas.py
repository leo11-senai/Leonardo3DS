#Listas

dias_Semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

gato = list('gato') #list separa em caracteres o str
print(gato)


dia_mes_ano = '22/05/2026'.split('/')
print(dia_mes_ano)

frutas_separadas = 'mamao,morango,maça'.split('/')
print(frutas_separadas)

texto_digitado = input('Digite texto: ')
texto_splitado = texto_digitado.split(' ')
print(texto_digitado)


print(dias_Semana[-1])
print(dias_Semana[1:6])