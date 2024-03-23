'''crie um programa que leia o (ano de nascimento) de (sete pessoas). no final ,
 mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''

from datetime import date
atual= date.today().year
tot_menor = 0 #acumuladores
tot_maior = 0 #acumuladores
for i in range(7):
    nasc = int(input(f'digite o {i+1}º ano de nascimento:'))
    idade = atual - nasc
    if idade >= 18:
        tot_maior = tot_maior + 1 #se eu botar print vai aparecer varios print embaixo de cada ano
        
    else:
        tot_menor = tot_menor + 1
print(f'tem {tot_menor} menores e {tot_maior} maiores')