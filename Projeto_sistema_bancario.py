""" Variáveis """ 

saldo = 500
historico = []
limite_saque = 500
LIMITE_SAQUES = 3
saques_realizados = 0

def obter_valor(mensagem):
    """ Solicita um valor numérico positivo ao usuário. """
    while True:
        valor = input(mensagem).replace(',', '.')
        try:
            valor = float(valor)
            if valor > 0:
                return valor
            print("Valor inválido! Insira um número positivo.")
        except ValueError:
            print("Entrada inválida! Digite um valor numérico.")

def exibir_menu():
    """ Exibe o menu de opções do sistema bancário. """
    print("\n==== MENU ====")
    print("[1] Sacar")
    print("[2] Depositar")
    print("[3] Saldo")
    print("[4] Extrato")
    print("[5] Opções")
    print("[6] Sair")

def exibir_opcoes():
    """ Exibe informações sobre o funcionamento do sistema. """
    print("\n==== OPÇÕES ====")
    print("1 - Sacar: Permite retirar dinheiro do saldo. Máximo R$500.00 por saque, até 3 saques diários.")
    print("2 - Depositar: Adiciona dinheiro ao saldo.")
    print("3 - Saldo: Exibe valor atual presente em conta.")
    print("4 - Extrato: Exibe todas as movimentações realizadas.")
    print("5 - Opções: Exibe este menu de ajuda.")
    print("6 - Sair: Fecha o sistema bancário.")

def realizar_saque():
    """ Realiza um saque, respeitando limite de valor e quantidade diária. """
    global saldo, saques_realizados

    if saques_realizados >= LIMITE_SAQUES:
        print("Limite de 3 saques diários atingido!")
        return

    saque = obter_valor('Qual valor deseja sacar? ')

    if saque > limite_saque:
        print("Limite máximo de saque R$500.00")
    elif saldo >= saque:
        saldo -= saque
        saques_realizados += 1
        historico.append(f"Saque: -R${saque:.2f}")
        print(f'Retirar o valor de R${saque:.2f} na boca do caixa!')
    else:
        print(f'Saldo insuficiente! Seu saldo atual é de R${saldo:.2f}')

def realizar_deposito():
    """ Realiza um depósito. """
    global saldo
    deposito = obter_valor('Quanto deseja depositar? ')
    
    saldo += deposito
    historico.append(f"Depósito: +R${deposito:.2f}")
    print(f'Você realizou um depósito de R${deposito:.2f}')

def exibir_extrato():
    """ Exibe o extrato bancário com todas as transações. """
    print("\n==== EXTRATO ====")
    
    if not historico:
        print("Nenhuma movimentação registrada.")
    else:
        for transacao in historico:
            print(transacao)
    
    print(f"\nSaldo atual: R${saldo:.2f}")

def exibir_saldo():
    """ Exibe o saldo atual. """
    print("\n==== SALDO ====")  
    print(f"\nSaldo atual: R${saldo:.2f}")

def sis_bank():
    """ Função principal do sistema bancário. """
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número entre 1 e 6.")
            continue

        if opcao == 1:
            realizar_saque()
        elif opcao == 2:
            realizar_deposito()
        elif opcao == 3:
            exibir_saldo()
        elif opcao == 4:
            exibir_extrato()
        elif opcao == 5:
            exibir_opcoes()
        elif opcao == 6:
            print("Saindo do sistema bancário...")
            break
        else:
            print("Opção inválida! Tente novamente.")

sis_bank()