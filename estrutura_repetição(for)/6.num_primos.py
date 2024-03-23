'''faça um programa que leia um (numero inteiro) e diga 
se ela é ou não um (número primo.)'''

num = int(input('digite um numero:'))
div = 0
for i in range(1, num + 1):#se o numero for divisivel pelo contador 
    if num % i == 0:
        print('\033[33m',end= ' ')#para cores no python 34 azul 
        div = div +1
    else:
        print('\033[31m',end= ' ')#para cores no python 33 amarelo, 31 vermelho 
    print(i,end=' ')#precisa da um print no for
print('\n\033[m')
print(f'o numero {num} é divisivel {div} vezes')#para um numero ser primo precisa ser divisivel 2 vezes 
if div == 2:
    print(f'sendo assim o numero {num} é primo!')

else:
    print(f'sendo assim o numero {num} não é primo!')