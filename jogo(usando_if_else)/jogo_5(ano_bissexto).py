#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('digite o ano:'))
calculo = ano % 4
if calculo == 0:
  print(f'o ano {ano}, é bisesexto')
else:
  print(f'o ano {ano}, não é bissexto')