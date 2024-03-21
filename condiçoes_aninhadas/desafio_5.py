#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# média abaixo de 5.0: reprovado
# média entre 5.0 e 6.4 recuperaçâo
# média 7.0 ou superior aprovado

from time import sleep
nota = float(input('digite sua nota:'))
print('\n')
nota2 = float(input('digite outra nota:'))
print('\n')
# media é soma das notas dividido pelo numero de notas
media = (nota + nota2) / 2
print('CARREGANDO...')
sleep(4)
print('\n')
if media >= 7.0:
    print('aprovado.')

elif media >= 5.0:
    print('recuperação')

else:
    print('reprovado.')
