'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint #importando um modulo , computador pensa em um numero
computador = randint(0, 10) # computador pensar entre 0 e 10 numeros inteiros
print('''
sou seu computador...
acabei de pensar em um numero entre 0 e 10.
será que você consegue adivinhar qual foi ?
      ''')
acertou = False #falso
palpite = 0
while not acertou: #enquanto não acerta
    jogador = int(input('qual seu palpite?'))
    palpite = palpite + 1
    if  jogador == computador :# se jogador for igual computador ( acertou )
        acertou = True #certo 
    else:
        if jogador < computador:# se jogador for menor que computador :
         print('maior... tente novamente')
        elif jogador > computador:# se jogador for maior que computador:
            print('menos... tente novamente')

print(f'acertou com {palpite} tentativas, parabens!')