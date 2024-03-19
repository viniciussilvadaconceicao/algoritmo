#escreva um programa que leia (dois números)inteiros e compare-os mostrando na tela um mensagem:
# o primeiro valor é maior 
# o segundo valor é maior
# não existe valor maior, os dois são (iguais)

from time import sleep
num = int(input('digite um numero:'))
print('\n')
num2 = int(input('digite outro numero:'))
print('\n')
print('PROCESSANDO...')
sleep(4)
print('\n')
if num > num2:
    print(f'o numero {num}, é maior')
elif num == num2:
    print('os numeros são iguais.')
else:
    print(f'o numero {num2} é maior.')