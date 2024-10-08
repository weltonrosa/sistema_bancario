''' 
Desafio Sistema Bancário 

Operação de depósito : 
- depositar valores positivos;
- não é necesário identificação de conta e agência
- todos os depósitos devem ser armazenados em uma variável e exibidos no extrato

Operação de saque: 
- apenas 3 saques diários
- limite máximo de R$ 500,00 por saque
- exibir mensagem informando que não é possivel sacar por falta de saldo
- todos os saques devem ser armazenados em uma variável e exibidos no extrato

Operação de extrato: 
- deve listar todos os depósitos e saques realizados
- exibir ao final o saldo atual da conta
- valores devem ser exibidos no formato R$ X.XXX, ex: 1500.45 = R$ 1500.45 
'''

import os

menu ="""
============= M E N U =============

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

====================================
=> """

LIMITE_SAQUES = 3
LIMITE_VALOR = 500
extrato = ""
saldo = 1000
numero_saques = valor = 0


def limpa_tela():
    os.system('cls')

while True:
    limpa_tela()    
    opcao = str(input(menu))
    
    if opcao == "1":
        limpa_tela()
        print("============= D E P O S I T O =============\n") 
        print(f"\tSaldo Atual => R$ {saldo:.2f}\n")       
        valor = float(input("Digite o valor do depósito R$ "))
        if valor > 0:
            saldo += valor
            extrato += "\nDeposito R$ " + str(valor)
        else:
            limpa_tela()
            print("=================== E R R O  ===================\n") 
            print("O Valor do depósito deve ser maior do que Zero.\n\nPressione <ENTER> para retornar ao menu.")
            input()

    elif opcao == "2":
        limpa_tela()
        print("=================== S A Q U E ===================\n")
        print(f"\tSaldo Atual => R$ {saldo:.2f}\n")  
        valor = float(input("Digite o valor do saque R$ "))
        if numero_saques < LIMITE_SAQUES:
            if valor > 0 and valor <= LIMITE_VALOR:
                numero_saques += 1
                saldo -= valor
                extrato += "\nSaque... R$ " + str(valor)
            else:
                limpa_tela()
                print("=================== E R R O  ===================\n")
                print(f" O valor limite para saque é R$ {LIMITE_VALOR:.2f}.\n\n")
                print("Pressione <ENTER> para retornar ao menu.\n")
                input()
        else:
            limpa_tela()
            print("=================== E R R O  ===================\n")
            print(" Você já atingiu ao limite de 3 saques por dia.\n\n")
            print("Pressione <ENTER> para retornar ao menu.\n")
            input()

    elif opcao == "3":
        limpa_tela()
        print("============= E X T R A T 0 =============\n\n")
        print(f"\t\t{extrato}\n")
        print(f"\tSaldo Atual R$ {saldo:.2f}\n\n")
        print("=========================================\n")
        print("Pressione <ENTER> para retornar ao menu.\n")
        input()
    elif opcao == "0":
        limpa_tela()
        print("Obrigado por utilizar nosso sistema.\n\n")
        break
    else:
        limpa_tela()
        print("\nOperação inválida, por favor selecione novamente a operação desejada.\n\nPressione <ENTER> tecla para retornar ao menu.")
        input()
        limpa_tela()