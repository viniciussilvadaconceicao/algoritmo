#o professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

#import random
#(shuffle) serve para embaralhar uma lista e botar com uma ordem todos eles

from random import shuffle
a = str(input('primeiro aluno:'))
b = str(input('segundo aluno:'))
c = str(input('terceiro aluno:'))
d = str(input('quarto aluno:'))
lista = [a, b, c, d]
shuffle(lista)
#random.shuffle(lista)
print('os alunos sorteados sera')
print(lista)
