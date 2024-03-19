#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
#import time

computador = randint(0,5)
usuario = int(input('digite um numero:'))
print('\n')
print('PROCESSANDO...')
sleep(3)
print('\n')
if usuario == computador:
  print('muito bem acertou parabens!')

else:
  print(f'perdeu... pensei no numero: {computador}')