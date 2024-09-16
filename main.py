menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""

saldo = 0 
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        valor_deposito = float(input("Qual valor você quer depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        print("Sacar")
        valor_saque = float(input("Qual valor você quer sacar? "))
        if numero_de_saques < LIMITE_SAQUES:
            if valor_saque > 0 and valor_saque <= saldo:
                saldo -= valor_saque
                numero_de_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para saque.")
        else:
            print("Limete de saques pro dia atingido")
    elif opcao == "e":
        print("Extrato")
        print("\n======== EXTRATO ========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================")
    elif opcao == "q":
        print("Sair")
        print("Encerrando...")
        break

    else:
        print("A letra inserida esta errado... digite novamente a letra certa!!")