'''desenvolva um programa que leia (seis número inteiros ) e 
mostre a soma apenas daqueles que forem (pares). se o valor digitado for (impar) desconsidere-o'''
soma = 0
cont = 0
for i in range(1,7):
        num = int(input(f'digite o {i}º numero:'))
        if num % 2 == 0:#se o numero for igual a zero(par) ira somar.
            soma = soma + num #para fazer a soma
            cont = cont + 1 # para conta os numeros 
print(f'a soma foi {soma}')