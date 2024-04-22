'''exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
valor1 = int(input('digite o primeiro valor:'))
valor2 = int(input('digite o segundo valor:'))
opçao = 0
while opçao != 5:
    print('''escolha uma das opçôes:
      [1] soma
      [2] multiplicação
      [3] maior
      [4] novos número
      [5] sair do programa
      ''')  
    opçao = int(input('qual foi sua opção:'))
    if opçao == 1:
        soma = valor1 + valor2
        print(f'a soma entre {valor1} e {valor2} é: {soma}')
    elif opçao == 2:
        multi = valor1 * valor2
        print(f'a multiplicção entre {valor1} e {valor2} é: {multi}')
    elif opçao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
           maior = valor2
           print(f'entre {valor1} e {valor2} o maior é {maior}')
    elif opçao == 4:
        print('informe os numeros novamente.')
        valor1 = int(input('digite o primeiro valor:'))
        valor2 = int(input('digite o segundo valor: '))

    elif opçao == 5:
        print('FINALIZANDO...')
    else:
        print('opção invalida')
    print('-=-'*20)
print('programa finalizado')