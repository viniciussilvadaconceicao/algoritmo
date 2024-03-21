nome = str(input('qual seu nome:'))
print('\n') 

if nome == 'vinicius':
    print('olá que nome bonito!')

#elif usamos em uma condiçao composta e o (or) significa ou nao pode esqueçer do :, == para igual
elif nome == 'maria' or nome == 'joao' or nome == 'paulo':
    print('seu nome é bem popular no Brasil.')

# o in sifnifica igual 
elif nome in 'andreza ana celma':
    print('que belo nome feminino!')

else:
    print('seu nome é bem normal.')
print('\n')
print(f'tenha um bom dia {nome}.')