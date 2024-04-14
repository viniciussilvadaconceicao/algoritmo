'''4. Escreva uma função recursiva que verifique se uma string é um palíndromo. Um
palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente,
ignorando espaços, maiúsculas e minúsculas. Por exemplo, "arara" é um palíndromo.'''
def inverter_string(a):
    a = a.replace("", "").lower()
    if a == '':
        return a
    else:
        return inverter_string(a[1:]) + a[0]

# Exemplo de utilização
str_inicial = "osso"
str_2= inverter_string(str_inicial)
print(str_2)
