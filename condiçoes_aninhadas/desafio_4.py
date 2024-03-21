#faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar 
#se já passou o tempo do alistamento 
#seu programa também devera monstra o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year

nasc = int(input('qual é o ano de seu nascimento:'))
print('\n')
idade = atual - nasc

print(f'quem nasceu em {nasc}, tem {idade} anos.')
print('\n')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')

elif idade < 18:
    saldo = idade - 18
    print(f'voce ainda vai se alistar falta {saldo}. ')

elif idade > 18:
    saldo1 = 18 - idade
    print(f'voçê ja passou {saldo1} anos do prazo de se alistar.')