#escreva um programa para aprovar o emprestimo bancario de uma casa. O programa vai perguntar o 
#(valor da casa) , o (salario do comprador) e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal sabendo que ele nao pode exceder 30% do salário ou então 
#o emprestimo será negado.

#import time usei somente uma funçao do modulo 

from time import sleep
valor_casa = float(input('qual o valor da casa R$:'))
salario = float(input('qual o salario do comprador R$:'))
ano = int(input('quantos anos quer pagar:'))
salario_meses = salario * 12
anos_meses = ano * 12
prestaçao = (valor_casa / anos_meses)
porcentagem = (salario * 30 / 100 )
print('\n')
print('PROCESSANDO...')
sleep(4)
print('\n')
#se a prestação foi igual ou maior que 30% ou maior do salario dara recusado
if prestaçao >= porcentagem:
    print(f'o emprestimo foi negado.')
else:
    print(f'aprovado você ira pagar durante {anos_meses} meses x parcelas de {prestaçao:.2f}R$')