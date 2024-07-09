def gerenciamento():
    print('='*70)
    print('''Bem vindo(a) caro bibliotecario(a) ao sitema de gerenciamento da biblioteca digital universitária.
digite o numero da opção que deseja escolher:
        
ATENÇÃO: lembre que para acessar uma das opções abaixo precisa digitar um numero:
          
          [1]''')

def menu_principal():
    from time import sleep
    print("="*70)
    print('''Bem vindo(a) ao meu sistema para uma biblioteca digital universitária. 
escolha o numero da opção que deseja acessar: 
          
ATENÇÃO: lembre que para acessar uma das opções abaixo precisa digitar um numero:
          
          [1] - Entra como bibliotecário
          [2] - Entra como estudante
          [3] - Sair 
          ''')
    print("="*70)
    try:
        opcao = int(input("digite o numero da opção desejada: "))
        if opcao == 1:
            gerenciamento()

        elif opcao == 2:
            estudante()

        elif opcao == 3:
            print('obrigado por usar o sitema criado por Fabio alves da Silva ')
            sleep(2)
            return
    except ValueError:
        print('ERRO, escolha uma das opçoes digitando o numero correspondente')

menu_principal()

    