#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente
# desse angulo
#import math
from math import radians, sin, cos, tan
angulo = float(input('digite o seu angulo'))
#seno = math.sin(math.radians(angulo))
#cos = math.cos(math.radians(angulo))
#tang = math.tan(math.radians(angulo))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('o angulo de {}\ntem o seno {:.2f}\ntem o cosseno {:.3f}\ne a sua tangente {:.3f} '.format(angulo, seno, cos, tang))