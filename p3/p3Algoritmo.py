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
            cadastra_livros()

        elif opcao == 2:
            cadastra_artigos()

        elif opcao == 3:
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

    