

'''desenvolver um algoritmo em Python que verifique se o livro solicitado está disponível na
biblioteca e, em caso afirmativo, registre o empréstimo, atualizando a
disponibilidade do livro.'''

'''A disponibilidade de cada livro é representada por uma variável
booleana chamada disponivel. Se o livro estiver disponível, o
valor será True; caso contrário, será False.
• O algoritmo deve receber como entrada o nome do livro
solicitado e o estado atual de disponibilidade dos livros.
• O algoritmo deve retornar uma mensagem indicando se o
empréstimo foi realizado com sucesso ou se o livro não está
disponível.'''

from time import sleep
livros = ['livro1', 'livro2', 'livro3', 'livro4', 'livro5']

def emprestimo():
    livro = str(input('escreva o nome do livro que deseja fazer o emprestimo: '))
    disponivel = True  
    if livro in livros and disponivel:
        print('livro emprestado com sucesso')
        sleep(3)
        livros.remove(livro)
        limpar_tela()
        return menu()
    else:
        print('Livro não disponivel')
        sleep(3)
        limpar_tela()
        return menu()

def limpar_tela():
    import os 
    os.system('cls'if os.name =='nt'else 'clear')


def menu():
    print('='*70)
    print('''Olá usuário bem vindo ao programa de emprestimo de livros
escolha uma das opções abaixo:
          
ATENÇÃO para escolher precisa digitar a opção com numero correspondente
          
          [1] livros
          [2] sair
          ''')
    print('='*70)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print('''Os livros disponiveis são:
              ''')
        for livro in livros:
            print(livro)
        print()
        emprestimo()

    elif opcao == 2:
        print('Obrigado por usar o sistema')
        sleep(3)
        return

menu()
    