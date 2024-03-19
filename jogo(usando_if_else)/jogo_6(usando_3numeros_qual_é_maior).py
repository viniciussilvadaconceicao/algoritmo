#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('digite o primeiro valor:'))
b = int(input('digite o segundo valor:'))
c = int(input('digite o terceiro valor:'))

menor = a
if b<a and b<c:
  menor = b
if c<a and c<b:
  menor = c

maior = a
if b>c and b>a:
  maior = b
if c>b and c>a:
  maior = c

print(f'o menor valor é: {menor}, o maior valor é: {maior}')