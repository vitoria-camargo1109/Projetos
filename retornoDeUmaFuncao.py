"""
Escreva uma função que retorne o maior valor entre dois números.
Valores esperados: maximo(5,6) = 6 maximo (12,12) = 12
"""

def maior_valor(x,y):
    if x > y:
        return x
    else:
        return y

print(maior_valor(5,6))

print(maior_valor(12,12))