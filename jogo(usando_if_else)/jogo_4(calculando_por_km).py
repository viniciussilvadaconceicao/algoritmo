#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('qual a distancia de uma viagem em km:'))
if km <= 200:
  total = 0.50 * km
  print(f'o preço da viagem vai custa {total}')
else:
  total2 = 0.45 * km
  print(f'o preço da viagem vai custar {total2} ')