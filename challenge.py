import os

NOME_BANCO = ' Mu Bank '
WITHDRAWAL_LIMIT = 500
OPTIONS = [1, 2, 3, 0]
remaining_withdrawals = 3
balance = 0
deposits = ''
withdrawals = ''

menu = f'''
{NOME_BANCO.center(50, '=')}

    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [0] - Sair

{''.center(50, '=')}
'''

while True:
    os.system('cls')
    print(menu)
    
    option = int(input('Digite a opção desejada: '))
    
    if option in OPTIONS:
        if option == 1:
            os.system('cls')
            print(f'{NOME_BANCO.center(50, '=')}\n')
            print(f'{"DEPÓSITO".center(50)}\n')

            value = float(input('Valor do depósito: R$'))

            if value > 0:
                balance += value
                deposits += f' + R${value:.2f}\n'
                print('\nDepósito realizado com sucesso!\n')
            else:
                print('\nValor inválido!\n')
            
            input('Pressione ENTER para voltar ao menu principal.')        

            print(f'\n{"".center(50, '=')}\n')
        elif option == 2:
            os.system('cls')
            print(f'{NOME_BANCO.center(50, '=')}\n')
            print('SAQUE'.center(50))
            
            value = float(input('Valor do saque: R$'))

            if value > 0:
                if value > WITHDRAWAL_LIMIT:
                    print('\nOperação não permitida!\n\nO valor escede seu limite por saque.\n')
                elif remaining_withdrawals == 0:
                    print('\nOperação não permitida!\n\nVocê atingiu a quantidade máxima de saques.\n')
                elif value > balance:
                    print('\nOperação não permitida!\n\nNão há saldo suficiente para realizar esta operação.\n')
                else:
                    remaining_withdrawals -= 1
                    balance -= value
                    withdrawals += f' - R${value:.2f}\n'
                    print('\nSaque realizado com sucesso!\n')
                        
            else:
                print('\nValor inválido!\n')
            
            input('Pressione ENTER para voltar ao menu principal.')        

            print(f'\n{"".center(50, '=')}\n')
        elif option == 3:
            os.system('cls')
            print(f'{NOME_BANCO.center(50, '=')}\n')
            print('EXTRATO'.center(50))
            
            if deposits or withdrawals:
                if deposits:
                    print('DEPÓSITOS')
                    print(deposits)
                
                if withdrawals:
                    print(f'\n{"".center(50, '*')}\n')
                    print('SAQUES')
                    print(withdrawals)

                print(f'SALDO ATUAL: R${balance:.2f}')
            else:
                print('\nNão foram realizadas movimentações.\n')

            print(f'\n{"".center(50, '=')}\n')
            input('Pressione ENTER para voltar ao menu principal.')
        else:
            os.system('cls')
            print('\nPrograma encerrado!')
            break
    else:
        print('\nOpção inválida!\n')
        input('Pressione ENTER para voltar ao menu principal.')