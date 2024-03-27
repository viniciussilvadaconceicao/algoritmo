'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo 
e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('Gerador de PA:')
print(20*'-=-')
primeiro = int(input('primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = primeiro #vai pular em numero de casas
cont = 1 #para contar ate 10 casas
while cont <= 10:
    print(f'{termo} - ',end= '')
    termo = termo + razão # atualizando o termo (antes da soma) 
    cont = cont + 1