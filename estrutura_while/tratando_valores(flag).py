'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
n = 0 # essa variavel criei para ter uma partida 
cont = 0 # essa variavel foi criada para contar quantos numeros foi inserido
soma = 0 # criei essa variavel para fazer a soma entre os numeros digitados 
n = int(input('digite um numero [considerando que 999 ira PARAR!]')) #usei o flag para não usar ele como numero (somando e contando)  
while n != 999: #criei essa condição de parada sabendo que n diferente de 999
    cont+=1 #essa variavel foi feita para somar quantos numeros foram inseridas 
    soma += n #essa variavel criei para somar os numeros entre eles 
    n = int(input('digite um numero [considerando que 999 ira PARAR!]'))#ele precisa vim para baixo das variavel e repetir acima do loop
print('\n')
print(f'FIM foram digitados {cont} numeros e a soma entre esses numeros deu {soma}')