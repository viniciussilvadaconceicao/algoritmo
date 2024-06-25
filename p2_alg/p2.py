from time import sleep

'''essa função vai adicionar livros na biblioteca'''
def add_livro():
    titulo = str(input('nome do livro: '))
    data = str(input('A data de quando fizeram o livro : '))
    tema = str(input('qual tema do livro : '))
    contexto = str(input('Qual contexto desse livro: '))
    descricao = str(input('Qual é a descrição do livro:'))
    autor = str(input('Quem é o autor desse livro: '))
    try:
        with open('livrosdabiblioteca.txt', 'a') as arquivo:
            arquivo.write(f'livro:{titulo}, data:{data}, tema:{tema}, contexto:{contexto}, descricao:{descricao}, autor:{autor}\n')
            print('Todas essas infomações foi inserida no sitema')
            sleep(3)
            return menu_inicial()
        
    except IOError:
        print('verifique o codigo tem um erro na entrada de dados')
        sleep(2)
        return menu_inicial()


'''essa função vai remover o livro desejado da biblioteca'''       
def rem_livro(titulo):
    try:
        with open('livrosdabiblioteca.txt', 'r') as arquivo:
            arquivo.readlines()
        with open('livrosdabiblioteca.txt', 'w') as arquivo:
            for i in arquivo:
                if titulo not in i:
                    arquivo.write(i)
            print('Livro foi removido do sistema com sucesso')
            sleep(2)
            return menu_inicial()

    except IOError:
        print('verifique o codigo tem um erro na entrada de dados')
        sleep(2)
        return menu_inicial()


'''essa função escolhi para ordenar '''
def bubble_sort(lista):
    lendo_lista = len(lista)
    for a in range(lendo_lista):
        for b in range(lendo_lista - a - 1):
            if lista[b] > lista[b + 1]:
                lista[b], lista[b + 1] = lista[b + 1], lista[b]
    return lista


'''essa função vai listar os livros da biblioteca'''

def lista_livros():
    try:
        with open('livrosdabiblioteca.txt', 'r') as arquivo:
            livros = arquivo.readlines()
            livros = [livro.strip().split(',') for livro in livros]
            livros_ordenados = bubble_sort(livros)
            for livro in livros_ordenados:
                print(livro)
                sleep(5)
            print('Programa ira retornar ')
            sleep(3)
            return menu_inicial()
    except IOError:
        print('livro não esta na lista')
        sleep(3)
        return menu_inicial()  
             
'''e essa função vai ser o meu menu principal'''
def menu_inicial():
    print()
    print('='*70)
    print('''Olá  bem vindo ao sistema de biblioteca virtual,
esse sistema foi feito com a intenção de ajudar o bibliotecario, 
nas suas tarefas do dia a dia. 
          
Escolha uma das opçoes abaixo para continuar:
Atenção: somente numeros seram aceitos.
          
[1] Adicionar livros
[2] Listar livros
[3] Remover livros
[4] sair
          ''')
    print('='*70)
    print()
    resp = int(input('Digite o numero que corresponde a sua resposta:'))
    if resp == 1:
        add_livro()
    elif resp == 2:
        lista_livros()
    elif resp == 3:
        titulo = str(input('qual o livro você deseja remover?, escreva o nome:'))
        rem_livro(titulo)
    elif resp == 4:
        print('Obrigado por usar nosso sistema de gerenciamento tchau...')
        sleep(2)
        return
    
menu_inicial()
print(menu_inicial)