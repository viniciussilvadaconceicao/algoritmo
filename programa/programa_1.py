#crie um programa que leia um número real qualquer pelo teclado
# e montre na tela a sua porção inteira
# ex: digite um número:6.127
# o numero 6.127 tem a parte inteira 6

from math import trunc
#import math
num = float(input('escreva um numero:'))
#inteiro = math.trunc(num)
inteiro = trunc(num)
print('o numero {} tem a parte inteira {}'.format(num, trunc(inteiro)))
#print('o numero {} tem a parte inteira {}'.format(num, math.trunc(inteiro)))

num = float(input('digite um numero:'))
print('numero que você digitou foi {}, e a parte inteira dele é {}.'.format(num, int(num)))