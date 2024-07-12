'''Um sistema de um aplicativo de delivery de comida precisa permitir que
os usuários adicionem itens ao carrinho de compras. Um dos casos de
uso é o "Adicionar Item ao Carrinho", onde um usuário pode selecionar
um item disponível no cardápio e adicionar ao seu carrinho'''
carrinho = []


def menu():
    print('='*70)
    print('''Olá usuário bem vindo ao aplicativo de delivery de comida
escolha uma das opções abaixo:
            
            [1] - Adicionar item ao carrinho
            [2] - Sair
          ''')
    print('='*70)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print('''Os itens disponiveis são:
              ''')
        itens = ['pizza', 'hamburguer', 'batata frita', 'refrigerante', 'sorvete']
        for item in itens:
            print(item)
        print()
        adicionar_item()
        
    elif opcao == 2:
        print('Obrigado por usar o sistema')
        return
