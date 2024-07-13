'''Um sistema de um aplicativo de delivery de comida precisa permitir que
os usuários adicionem itens ao carrinho de compras. Um dos casos de
uso é o "Adicionar Item ao Carrinho", onde um usuário pode selecionar
um item disponível no cardápio e adicionar ao seu carrinho'''
carrinho = []

def adicionar_item():
    produto = ['pizza', 'hamburguer', 'açai', 'sushi', 'churrasco-misto']
    print('''Os produtos disponiveis são:
          ''')
    for item in produto:
        print(item)
    print()
    item = str(input('Digite o nome do item que deseja adicionar ao carrinho: '))
    carrinho.append(item)
    rsp = str(input('Quer adicionar outros produtos no carrinho? se sim digite S ou se não digite N  ')).upper()
    if rsp == 'S':
        adicionar_item()
    else:
        print('''Item adicionado com sucesso!
os itens são:''')
        for item in carrinho:
            print(item)

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
        adicionar_item()
        
    elif opcao == 2:
        print('Obrigado por usar o sistema')
        return

menu()

