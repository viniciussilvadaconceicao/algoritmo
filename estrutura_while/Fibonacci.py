'''Escreva um programa que leia um número N inteiro qualquer 
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''

'''0 + 1 = 1 + 1 = 2 + 1 = 3 + 5 = 8/'''
'''a fibonate é um termo mais outro termo gerando um novo termo assim continuando esse loop  
ex: 0  +   1  =  1  + 1  =  2 +  1 =  3 +  5 =  8 total de 7 termos se for o informado 
    t1    t2    t3  
          t1    t2    t3  nessa linha o contador iria andar para começa o laço somando os termos até chegar no ultimo termo
                          assim o t1 vira o t2 e o t2 vira o t3 para fazer toda a soma nessa repetição  '''    

n = int(input('digite o numero inteiro de contadores:'))

t1 = 0
t2 = 1

print(f'{t1} - {t2} -',end=' ')
cont = 3 #esse contador é 3 pois comecar depois dos 3 contadores no caso o 0 , 1 e a soma entre eles que da 1 
while cont <= n:
    cont += 1 # essa variavel seria a soma apartir do contato 3 soma ele mais 1 
    t3 = t1 + t2 
    t1 = t2 # dessa forma consigo andar com minha formula até chegar no ultimo termo informado
    t2 = t3 # assim consigo fazer a soma de 2 termos até chegar no ultimo 
    print(f'{t3} -',end=' ')
print('FIM')    
