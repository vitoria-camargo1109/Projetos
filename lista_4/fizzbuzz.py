"""
Escreva um programa em Python que percorra os números de 1 a 10 utilizando
um laço for. Para cada iteração, calcule o dobro do número atual.
Em seguida, utilize as estruturas if, elif e else combinadas
com o operador de módulo (%) para verificar as seguintes
condições e exibir a mensagem correspondente:

Se o dobro do número for divisível simultaneamente
por 3 e por 4, exiba a mensagem: "O número [valor] é múltiplo de 3 e 4".

Se for divisível apenas por 3, exiba: "Múltiplo de 3".

Se for divisível apenas por 4, exiba: "Múltiplo de 4".

Caso não atenda a nenhuma das condições acima,
exiba apenas o valor calculado do dobro.
"""

for num in range(1, 11):
    num_dobro = num * 2

    if num_dobro % 3 == 0:
        if num_dobro % 4 == 0:
            print(f"O número {num_dobro} é múltiplo de 3 e 4!")

    elif num_dobro % 3 == 0:
        print(f"O número {num_dobro} é múltiplo de 3!")

    elif num_dobro % 4 == 0:
        print(f"O número {num_dobro} é múltiplo de 4!")

    else:
        print(num_dobro)

    print()