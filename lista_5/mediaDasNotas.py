"""
Manipulando Listas (Média das Notas)
Escreva uma função chamada calcular_media que receba uma lista de números
como parâmetro. A função deve calcular e retornar a média desses valores.

Desafio extra: Se a lista estiver vazia, faça a função retornar 0 para
evitar erros de divisão por zero.
"""

def calcular_media(lista):

    soma = 0

    if len(lista) == 0:
        return 0

    for numero in lista:
        soma += numero
    media = soma / len(lista) #len(list) = A quantidade de índice.
    return media

lista = [2, 2, 2, 2, 2]

print(calcular_media(lista))



