 #elabore um programa que calcule o valor a ser pago por um produto, considerando o seu (preço normal) 
#(condiçao de pagamento:)
#a vista dinheiro/cheque: 10% de desconto
#á vista no crtão:5% de desconto 
#em até 2x no catrão: preço normal
#3x ou mais no cartão:20% juros
from time import sleep

valor = float(input('digite o valor do produto: R$'))
print('\n')
print('''escolha uma das opções para pagamento:
      
[1] dinheiro / cheque
[2] cartão debito 
[3] cartão 2x 
[4]cartão 3x ou mais''')
print('\n')
opçao = int(input('sua escolha:'))
print('\n')
print('PROCESSANDO...')
sleep(4)
print('\n')
if opçao == 1:
    desconto =( valor * 10 / 100 ) - valor
    print(f'voce tera um desconto de 10% preço do produto sera: {desconto}')

elif opçao == 2:
    desconto1 = (valor * 5 / 100 ) - valor
    print(f'pagando no cartão de debito tera um desconto de 5% sendo assim seu preço é {desconto1}')

elif opçao == 3:
    print(f'pagando em 2x no cartão o preço sera {valor} sem alteração de juros ou desconto')

else:
    a = valor * 20 / 100 + valor 
    print(f'pagando 3x ou mais,  tera um acrescimo de 20% sendo seu novo preço {a} .')
    