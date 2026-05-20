#condicionais 
# ou estruturas de controle

idade = int(input('Qual é sua idade? '))

if idade >= 18:
    print('Maior de idade!')
else:
    print ('Menor de idade!')
    


nota = int(input('Digite sua nota:'))
pc_presenca = 75

if nota == 60 and pc_presenca >= 75:
    print ('Aprovado')
elif nota >= 50 and pc_presenca >= 75:
    print ('Recuperação')
else:
    print('Reprovado!')