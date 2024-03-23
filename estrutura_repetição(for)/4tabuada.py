'''refaça o desafio 09 mostrando a (tabuada) de um numero que o usuário escolher só que agora utilizando 
o laço (for)'''

from time import sleep
num = int(input('digite um numero que deseja saber a tobuada:'))
print(14*'-=')
for c in range(1,11):
    mult = num * c
    print(f'{num} x {c} = {mult}')
print(14*'-=')