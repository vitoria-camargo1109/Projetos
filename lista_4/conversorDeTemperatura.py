"""
Um sistema meteorológico registra temperaturas em graus Fahrenheit na seguinte lista:
temperaturas_f = [32, 68, 100, 14, 85]. Escreva um programa que passe
por cada temperatura usando a estrutura for. Para cada iteração, aplique a
fórmula aritmética para converter o valor para
Celsius: C = ((f - 32) * 5)/9. Após calcular a conversão, classifique e
imprima a sensação térmica utilizando if, elif e else de acordo com os
critérios abaixo:
Se a temperatura em Celsius for menor que 15, exiba "Frio".
Se a temperatura estiver entre 15 e 25 (inclusive), exiba "Agradável".Se for
estritamente maior que 25, exiba "Quente".
"""

def celsius(f):
    celsius = ((f - 32) * 5) / 9
    return celsius

temperaturas_f = [32, 68, 100, 14, 85]

for temp in temperaturas_f:
    print(celsius(temp))





