#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será 
#(base da conversão):
#-1 para binário
#-2 para octal
#-3 para hexadecimal

from time import sleep
num = int(input('digite um numero:'))
print('\n')
print('''escolha uma das base para converter:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
print('\n')
opcao = int(input('sua escolha:'))
print('\n')
print('PROCESSANDO...')
sleep(4)
print('\n')
if opcao == 1:
    num_bin = bin(num)
    print(f'o numero {num}, em BINÁRIO é igual a {num_bin}!')
elif opcao == 2:
    num_octal = oct(num)
    print(f'o numero {num}, em OCTAL é igual a {num_octal}! ')
elif opcao == 3:
    num_hexa = hex(num)
    print(f'o numero {num}, em HEXADECIMAL é igual a {num_hexa}!')
else:
    print('opção invalida!')