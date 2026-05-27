"""
Considere a seguinte lista contendo os salários base dos funcionários de uma empresa:
salarios = [1200, 2500, 3200, 5000, 800]. Crie um script que utilize um laço for
para iterar sobre cada valor da lista. Calcule e exiba o novo salário atualizado
de cada funcionário aplicando as seguintes regras através das estruturas if,
elif e else:

Salários inferiores a 1500 recebem um aumento de 20%.

Salários maiores ou iguais a 1500 e menores que 3000 recebem um aumento de 10%.

Salários de 3000 ou mais não recebem aumento percentual, mas
ganham um bônus fixo de 250 adicionado ao valor base.
"""

novo_salario = 0
salario = [1200, 2500, 3200, 5000, 800]

for valor in salario:
        if valor < 1500:
            novo_salario = valor + (valor * 0.20)
            print(f"O valor do novo é {novo_salario:.2f}")

        elif valor >= 2500 and valor < 3000:
            novo_salario = valor + (valor * 0.10)
            print(f"O valor do novo é {novo_salario:.2f}")

        else:
            novo_salario = valor + 250
            print(f"O valor do novo é {novo_salario:.2f}")