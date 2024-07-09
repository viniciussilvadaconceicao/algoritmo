def estudante():
    from time import sleep
    print('='*80)
    print('''Bem vindo(a) estudande, ao sitema da biblioteca digital universitária.
escolha o numero da opção que deseja acessar: 
          
ATENÇÃO: lembre que para acessar uma das opções abaixo precisa digitar um numero:
          
          [1] - livros
          [2] - artigos científicos
          [3] - teses 
          [4] - retorna
          ''')
    print('='*80)
    try:
        opcao = int(input("digite o numero da opção desejada: "))
        if opcao == 1:
            limpar_tela()
            lista_livros()
            sleep(8)

        elif opcao == 2:
            limpar_tela()
            lista_artigos()
            sleep(8)

        elif opcao == 3:
            limpar_tela()
            lista_teses()
            sleep(8)

        elif opcao == 4:
            return menu_principal()
        
    except ValueError:
        print('ERRO, escolha uma das opçoes digitando o numero correspondente')

def lista_teses():
    from time import sleep
    try:
        with open('tese.txt', 'r') as arquivo:
            tese = arquivo.readlines()
            tese = [tese.strip().split(',') for tese in tese]
            tese_ordenados = bubble_sort(tese)
            for tese in tese_ordenados:
                print(tese)
                sleep(5)
            print('Programa ira retornar ')
            sleep(3)
            return menu_principal()
    except IOError:
        print('ERRO, livro não foi encontrado na lista')
        sleep(3)
        return menu_principal()
    
def lista_livros():
    from time import sleep
    try:
        with open('livrosdigital.txt', 'r') as arquivo:
            livros = arquivo.readlines()
            livros = [livro.strip().split(',') for livro in livros]
            livros_ordenados = bubble_sort(livros)
            for livro in livros_ordenados:
                print(livro)
                sleep(5)
            print('Programa ira retornar ')
            sleep(3)
            return menu_principal()
    except IOError:
        print('livro não esta na lista')
        sleep(3)
        return menu_principal()  

def  bubble_sort(lista):
    lendo_lista = len(lista)
    for a in range(lendo_lista):
        for b in range(lendo_lista - a - 1):
            if lista[b] > lista[b + 1]:
                lista[b], lista[b + 1] = lista[b + 1], lista[b]
    return lista

def limpar_tela():
    import os 
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastra_artigos():
    from time import sleep
    print('='*80)
    print('Bem vindo ao cadastro de artigos científicos da biblioteca digital universitária. ')
    print('='*80)
    try:
        artigo = str(input('digite o titulo do livro: '))
        with open('artigo.txt', 'a') as arquivo:
            arquivo.write(f'artigo:{artigo}\n')
            print('Todas essas infomações foi inserida no sitema')
            sleep(3)
            return gerenciamento()
        
    except ValueError:
        print('ERRO, digite o ano de publicação do livro em numeros')

def cadastra_livros():
    from time import sleep
    print('='*80)
    print('Bem vindo ao cadastro de livros virtuais da biblioteca digital universitária. ')
    print('='*80)
    try:
        titulo = str(input('digite o titulo do livro: '))
        autor = str(input('digite o nome do autor do livro: '))
        disciplina = str(input('digite a disciplina do livro: '))
        with open('livrosdigital.txt', 'a') as arquivo:
            arquivo.write(f'titulo:{titulo}, autor:{autor}, disciplina:{disciplina}\n')
            print('Todas essas infomações foi inserida no sitema')
            sleep(3)
            return gerenciamento()
        
    except ValueError:
        print('ERRO, digite o ano de publicação do livro em numeros')

def cadastra_teses():
    from time import sleep
    print('='*80)
    print('Bem vindo ao cadastro de teses da biblioteca digital universitária. ')
    print('='*80)
    try:
        tese = str(input('digite o nome da tese: '))
        with open('tese.txt', 'a') as arquivo:
            arquivo.write(f'tese:{tese}\n')
            print('Todas essas infomações foi inserida no sitema')
            sleep(3)
            return gerenciamento()
        
    except ValueError:
        print('ERRO, digite o ano de publicação do livro em numeros')

def gerenciamento():
    print('='*80)
    print('''Bem vindo(a) caro bibliotecario(a) ao sitema de gerenciamento da biblioteca digital universitária.
digite o numero da opção que deseja escolher:
        
ATENÇÃO: lembre que para acessar uma das opções abaixo precisa digitar um numero:
          
          [1] cadastra livros virtual
          [2] cadastra artigos científicos
          [3] cadastra teses e dissertações
          [4] retornar
          ''')
    print('='*80)
    try:
        opcao = int(input("digite o numero da opção desejada: "))
        if opcao == 1:
            limpar_tela()
            cadastra_livros()

        elif opcao == 2:
            limpar_tela()
            cadastra_artigos()

        elif opcao == 3:
            limpar_tela()
            cadastra_teses()

        elif opcao == 4:
            return menu_principal()
        
    except ValueError:
        print('ERRO, escolha uma das opçoes digitando o numero correspondente')

def menu_principal():
    from time import sleep
    print("="*80)
    print('''Bem vindo(a) ao meu sistema para uma biblioteca digital universitária. 
escolha o numero da opção que deseja acessar: 
          
ATENÇÃO: lembre que para acessar uma das opções abaixo precisa digitar um numero:
          
          [1] - Entra como bibliotecário
          [2] - Entra como estudante
          [3] - Sair 
          ''')
    print("="*80)
    try:
        opcao = int(input("digite o numero da opção desejada: "))
        if opcao == 1:
            limpar_tela()
            sleep(3)
            gerenciamento()
            
        elif opcao == 2:
            limpar_tela()
            sleep(3)
            estudante()
            

        elif opcao == 3:
            print('obrigado por usar o sitema criado por Fabio alves da Silva ')
            sleep(2)
            return
    except ValueError:
        print('ERRO, escolha uma das opçoes digitando o numero correspondente')

menu_principal()

    