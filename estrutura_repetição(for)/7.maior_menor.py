'''faça um programa que leia o (peso) de (cinco pessoas) , no final , mostre 
qual foi o (maior) e o (menor) peso lidos .'''

maior = 0 #acumuludor
menor = 0
for i in range(5):
    peso = float(input(f'digite o {i+1}º seu peso:'))
    if i == 1 :
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso  
        if peso < menor:
            menor = peso           
print(f'o maior peso foi {maior} e o menor foi {menor}')