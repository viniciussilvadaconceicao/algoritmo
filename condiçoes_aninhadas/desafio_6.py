#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria , de acordo com a idade:
#até 9 anos: MIRIM
#até 14 anos : INFANTIL
#até 19 anos : JUNIOR
#até 20 anos :SENIOR
#acima :MASTER

from datetime import date
from time import sleep
atual = date.today().year

nasc = int(input('qual ano você nasceu:'))
idade = atual - nasc

print('\n')
print('PROCESSANDO..')
sleep(4)
print('\n')

if idade <= 9:
    print('sua categoria é MIRIM')

elif idade <= 14:
    print('sua categoria é INFANTIL.')

elif idade <= 19:
    print('sua categoria é JUNIOR.')

elif idade == 20:
    print('sua categoria é MASTER.')

else:
    print('sua categoria é MASTER.')