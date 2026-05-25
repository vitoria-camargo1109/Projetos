"""Um cliente possui R$ 500,00 de saldo. Leia o valor de um
saque e informe se a transação foi permitida ou
se o saldo é insuficiente."""

saldo = 500.00
saque = float(input("Informe o valor do saque desejado: "))

if saque <= saldo:
    print("Sua transação foi permitida com sucesso!")
else:
    print("Saldo insuficiente!")