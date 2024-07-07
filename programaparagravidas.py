def mesesGravides():
    from time import sleep
    print('='*60)
    print('''Bem-vinda ao programa para grávidas!
Aqui você poderá saber quantos meses e semanas de gravidez você tem.''')
    print('='*60)
    semana = int(input('Digite quantas semanas de gravidez você está: '))
    meses = semana // 4
    semanas = semana % 4
    try:
        if meses < 1:
            print(f'Você ainda não completou um mês de gravidez. Está com {semanas} semana(s).')
            print('='*60)
        
        elif meses == 1:
            if semanas == 0:
                print(f'Você está com 1 mês de gravidez.')
            else:
                print(f'Você está com 1 mês e {semanas} semana(s) de gravidez.')
            print('='*60)
        
        elif meses > 1:
            if semanas == 0:
                print(f'Você está com {meses} meses de gravidez.')
            else:
                print(f'Você está com {meses} meses e {semanas} semana(s) de gravidez.')
            print('='*60)
        
        else:
            print('Valor inválido. Tente novamente.')
            sleep(2)

    except ValueError:
        print('ERRO, digite somente números inteiros sem vírgula. Tente novamente.')
        sleep(2)

mesesGravides()