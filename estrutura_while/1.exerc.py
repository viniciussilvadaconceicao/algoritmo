'''Exercício Python 1: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
#stip() para eliminar os espaços, upper() para botar maiusculo fm
sexo = str(input('digite o seu sexo F/M:')).strip().upper() [0]
# while(enquanto) pois não sei quantas vezes vai acontecer , not in(não,estiver)
while sexo not in 'MmFf':
     #esta mensagem vai aparecer novamente repetindo ate inserir a correta 
     sexo = str(input('dados invalidos. digite o seu sexo F/M:')).strip().upper() [0]
print(f'sexo {sexo} registrado com sucesso! ')