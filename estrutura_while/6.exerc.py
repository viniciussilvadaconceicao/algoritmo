'''Exercício Python 62: Melhore o DESAFIO 61, 
perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA:')
print(20*'-=-')
primeiro = int(input('digite o termo da PA:'))
razao = int(input('razão da PA:'))
print('\n')
termo = primeiro
cont = 1
total = 0
mais = 10 # variavel 
while mais != 0: # enquanto a variavel mais for diferente de 0 vai inserir mais termos 
    total = total + mais #para começar o programa com 10 elementos
    while cont <= total:
        print(f'{termo} - ',end= ' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA.')
    mais = int(input('desaja mostra mais algum termo?'))
print(f'FIM!, progreção finalizada com {total} termos totalizada')
