"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros"""

valor_produto = float(input("Digite o valor do produto: "))

print("Escolha a forma de pagamento abaixo: ")
print("------------------------------------------------")
print("1 - À vista dinheiro/cheque: 10% de desconto;\n"
      "2 - À vista no cartão: 5% de desconto;\n"
      "3 - Em até 2x no cartão: preço formal;\n"
      "4 - 3x ou mais no cartão: 20% de juros.\n"
      "------------------------------------------------")

escolha = int(input("Escolha: "))

if escolha == 1:
    valor_final = valor_produto - (valor_produto * 0.10)
elif escolha == 2:
    valor_final = valor_produto - (valor_produto * 0.05)
elif escolha == 3:
    valor_final = valor_produto
elif escolha == 4:
    valor_final = valor_produto + (valor_produto * 0.20)
else:
    valor_final = 0
    print("Forma de pagamento inválida.")

if valor_final != 0:
    print(f"O valor final dessa compra é de: R${valor_final:.2f}")

