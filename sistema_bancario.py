menu = "MENU".center(100, "#") + """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

-->"""

saldo = 0
extrato = ""
LIMITE_SAQUE_DIARIO = 500
numero_saques_diario = 0
LIMITE_NUMERO_SAQUES_DIARIO = 3

def deposito():
    global saldo
    global extrato
    valor_deposito = float(input("Qual valor você vai depositar? "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"DEPÓSITO: R$ {valor_deposito:6.2f}\n"
    else:
        print("O valor informado para depósito não pode ser negativo!")

def saque():
    global saldo
    global extrato
    global numero_saques_diario
    valor_saque = float(input("Qual valor você vai sacar? "))

    saldo_induficiente = valor_saque > saldo

    limite_excedido = valor_saque > LIMITE_SAQUE_DIARIO

    numero_saques_excedido = numero_saques_diario >= LIMITE_NUMERO_SAQUES_DIARIO

    if saldo_induficiente:
        print(f"Você não tem saldo suficiente para esse saque. Saldo: R$ {saldo:.2f}")
    elif limite_excedido:
        print(f"O valor do saque é maior que o limite diário. Limite: {LIMITE_SAQUE_DIARIO}")
    elif numero_saques_excedido:
        print(f"Você alcançou o número máximo de saques. Limite: {numero_saques_diario}")
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"SAQUE: R$ {valor_saque*-1:6.2f}\n"
        numero_saques_diario += 1
    else:
        print("O valor informado para saque não pode ser negativo!")

def exibe_extrato():
    print("EXTRATO".center(100, "="))
    print(extrato)
    print("".center(100, "-"))
    print(f"SALDO: {saldo:6.2f}")
    print("".center(100, "="))

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("DEPÓSITO".center(100, "#"))
        deposito()
    elif opcao == 2:
        print("SAQUE".center(100, "#"))
        saque()
    elif opcao == 3:
        exibe_extrato()
    elif opcao == 0:
        break
    else:
        print("Opção inválida!\nSelecione uma das opções propostas para continuar.")

print("Obrigado por ser nosso cliente!")