'''
AULA 02:

- Explicação da lista de exercícios anterior.
- Testar todas as funções de uma lista.

1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
Extra: Depois adicione em uma função.
'''

def criar_vetor(n:int) -> list:
   lista = []
   for i in range(n):
      numero = int(input(f'digite o {i+1}° numero:'))
      lista.append(numero)
   
   return lista
   
resultado = criar_vetor(5)
print(resultado)
