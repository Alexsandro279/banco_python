def exibir_menu():
    print("=== Banco Python do Alex===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))
    return opcao 

saldo = 0
limite = 600
extrato = ""
LIMITE_SAQUES = 3
numero_saques = 0

while True:
    opcao = exibir_menu()


    if opcao == 1:
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == 2:
        valor = float(input("Valor do saque: "))

        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor excede o limite por saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == 3:
        print("\n=== Extrato ===")
        print("Sem movimentações." if extrato == "" else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == 4:
        print("Saindo do sistema... Obrigado por usar nosso banco!")
        break

    else:
        print("Opção inválida. Tente novamente.")
""