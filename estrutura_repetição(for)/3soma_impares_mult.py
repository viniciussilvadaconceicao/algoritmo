'''faça um programa que calcule a (soma) entre todos os (numeros impares)
que são (múltiplos de 3) e que se encontram no intervalo de (1 até 500)'''
soma = 0 # acumuladores para fazer soma
cont = 0
for c in range(1,501,2):
    if c % 3 == 0: #para saber os multiplos de 3
        cont = cont + 1 #para fazer a conta
        soma = soma + c # para fazer a soma 
print(f'a soma dos multipos de 3 é: {soma} e sua conta é {cont}')#print precisa esta fora pois se não vai entra np range
