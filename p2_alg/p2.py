from time import sleep

'''essa função vai adicionar livros na biblioteca'''
def add_livro(titulo,data,tema,contexto,descricao,autor):
    try:
        with open('livrosdabiblioteca.txt', 'a') as arquivo:
            '''título, data de produção, tema, contexto histórico, descrição, autor'''
            arquivo.write(f'livro:{titulo}, data:{data}, tema:{tema}, contexto:{contexto}, descricao:{descricao}, autor:{autor}')
            print('Todas as infomações fornecidas foram inseridas no sitema com sucesso')
            sleep(9)
            return menu_inicial()
        
    except IOError:
        print('Erro de entrada de dados , por favor tente novamente')
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
        print('Erro na entrada de dados, por favor verifique e tente novamente')
        sleep(2)
        return menu_inicial()


'''essa função vai ordenar a lista de livros da biblioteca'''
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
                print(f'Título: {livro} ')
                sleep(1)
            print('Programa ira retornar ')
            sleep(2)
            return menu_inicial()
    except IOError:
        print("Erro ao abrir o arquivo, (ENTRADA OU SAÍDA DEU ERRO.)")
        sleep(3)
        return menu_inicial()  
             
'''e essa função vai ser o meu menu principal'''
def menu_inicial():
    print()
    print('='*70)
    print('''Olá seja bem vindo ao sistema de gerenciamento da biblioteca virtual,
esse sistema foi criado com a intenção de ajudar o bibliotecario, 
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
        '''título, data de produção, tema, contexto histórico, descrição, autor'''
        titulo = str(input('Digite o nome do livro que deseja adicionar na biblioteca virtual: '))
        data = str(input('Digite a data de produção do livro que deseja adicionar na biblioteca virtual: '))
        tema = str(input('Digite o tema do livro que deseja adicionar na biblioteca virtual: '))
        contexto = str(input('Digite o contexto histórico do livro que deseja adicionar na biblioteca virtual: '))
        descricao = str(input('Digite a descrição do livro que deseja adicionar na biblioteca virtual: '))
        autor = str(input('Digite o nome do autor do livro que deseja adicionar na biblioteca virtual: '))
        add_livro(titulo,data,tema,contexto,descricao,autor)
    elif resp == 2:
        lista_livros()
    elif resp == 3:
        titulo = str(input('digite o nome do livro que deseja remover da biblioteca virtual:'))
        rem_livro(titulo)
    elif resp == 4:
        print('Obrigado por usar nosso sistema de gerenciamento tchau...')
        sleep(2)
        return
    
menu_inicial()
print(menu_inicial)