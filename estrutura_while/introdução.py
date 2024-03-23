n = 1 #para iniciar
par = impa = 0
while n != 0:#enquanto n for diferente de 0 o programa vai continuar rodando
    n = int(input('digite um numero:'))
    if n != 0:
        if n % 2 == 0: #todo numero resto de 2 de 0 é par
            par += 1
        else:
            impa += 1# todo resto de numero que der 1 é impa
print(f'você digitou {par} numeros par e {impa} numeros impares.')