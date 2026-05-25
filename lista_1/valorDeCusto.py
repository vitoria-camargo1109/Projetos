"""Exercício 2.2: O custo ao consumidor de um carro novo é a soma do custo
de fábrica com a porcentagem do revendedor e com o custo dos impostos
(aplicados ao custo da fábrica). Supondo que a porcentagem do
revendedor seja de 25% do custo de fábrica e que os impostos custam 45% do
custo de fábrica, faça um algoritmo que leia o valor de custo de fábrica e
determine o preço do automóvel para o consumidor."""

custo_fabrica = float(input("Digite o custo de fábrica do carro:"))

porcentagem_revendedor = 0.25 * custo_fabrica
impostos = 0.45 * custo_fabrica

custo_novo = custo_fabrica + porcentagem_revendedor + impostos

print(f"O preço do automóvel será: R${custo_novo:.2f}")