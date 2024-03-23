'''faça um programa que mostre na tela uma contagem regressiva para o estouro 
de fogos artificio indo de (10 até 0),
com uma pausa de (1 segundo entre eles.) '''
from time import sleep
print('\n')
print('contagem regressiva para o estouro dos fogos!')
print('\n')
sleep(1) 
for i in range(10,-1,-1):
    print(f'{i}')
    sleep(.5)
print('BOW BOW BAAW')