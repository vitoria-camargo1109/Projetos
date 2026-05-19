"""
Escreva uma função que receba dois números e
retorne True se o primeiro número for múltiplo do segundo.
Valores esperados: multiplo(8,4) = True multiplo (7,3) = False
"""

def multiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False

print(multiplo(8, 4))

print(multiplo(7,3))