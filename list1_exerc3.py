'''3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
Extra: Se média maior ou igual a 7 mostrar "aprovado" se não mostrar "reprovado".'''
notas = []
n = 4
for i in range(n):
    nota = float(input(f'digite a {i+1}° nota:'))
    notas.append(nota)

somatorio = sum(notas)
media = somatorio / n

print(f'as notas são {notas} ')
print(f'a sua media é {media}')

if media >= 7:
    print('aprovado')

else:
    print('reprovado')