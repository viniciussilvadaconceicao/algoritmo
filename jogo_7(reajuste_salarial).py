#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('qual seu salário:'))
if salario < 1250:
  aumento = (salario * 15 ) / 100 +salario
  print(f'com aumento de 15% seu novo salario é {aumento}')
else:
  aumento1 = (salario * 10) / 100 + salario
  print(f'o aumento é de 10% seu novo salario é {aumento1}')