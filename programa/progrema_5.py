#faça um programa que leia comprimento do cateto oposto e do cateto adjacente de um TRIANGULO RETANGULO,
#calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('digite o numero do cateto oposto:'))
ca = float(input('digite o numero do cateto adjacente:'))
#co1 = math.pow(co,2)
#ca1 = math.pow(ca,2)
#soma = ca1 + co1
#raiz = math.sqrt(soma)
#pc = math.ceil(raiz)
hip = math.hypot(co, ca)
print('o comprimento da hipotenusa  de um triangulo retangulo é: {:.1f}'.format(hip))

co = float(input('digite o numero do cateto oposto'))
ca = float(input('digite o numero do cateto adjacente'))
hip = (co**2 + ca**2) ** (1/2)
print('o valor da hipotenusa de um triangulo retangulo é {:.1f}'.format(hip))