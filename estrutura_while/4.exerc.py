'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''
n = int(input('digite o numero para saber o fatorial:'))
c = n
f = 1 #para fazer os numero multiplica entre eles
print(f'fatorial {n}! =', end=' ')
while c > 0:
    print(f'{c}',end= ' ')
    print('x' if c > 1 else '=',end= ' ')
    f = f * c #a mult precisa esta na frente dos numeros
    c = c - 1 
print(f'{f}')