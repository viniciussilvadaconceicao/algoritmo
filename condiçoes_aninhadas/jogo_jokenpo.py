#crie um programa que faça o computador jogar jokenpo com você. pedra papel e tesoura
from random import randint
from time import sleep
item = ('pedra', 'papel', 'tesoura' )
computador = randint(0, 2)
print('''escolha uma das opções:
      
      [0] pedra
      [1] papel 
      [2] tesoura ''')
print('\n')

opçao = int(input('digite sua escolha:'))
print('\n')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('\n')
if computador == opçao:
    print('parabens voçe acertou')
else:
    print('errou tente novamente')