'''desenvolva um programa que leia o (nome, idade e sexo) de ( 4 pessoas).
no final do programa , mostre:
(a media de idade) do grupo.
qual o nome do homem (mais velho)
quantas mulheres tem (mais de 20 anos)'''

somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomemaisvelho = ''
totmulher20 = 0

for i in range(4):
    print(f'----- A {i+1}º PESSOA-----')
    nome = str(input('nome:')).strip()
    idade = int(input('idade:'))
    sexo = str(input('sexo (M/F):')).strip()
    somaidade = somaidade + idade
    if i == 1 and sexo in 'Mm': 
        maioridadehomen = idade 
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = mediaidade + somaidade / 4
  
    
print(f' a media de idade é {mediaidade} nome do mais velho {nomemaisvelho} idade {maioridadehomen} ')
print(f'ao todo são {totmulher20} com menos de 20 anos. ')