'''5. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro
positivo.'''
def soma(a, b):
    if b == 0:  
        return a
    else:
        return soma(a + 1, b - 1) 

a = 6
b = 4
resultado = soma(a, b)
print(resultado)
