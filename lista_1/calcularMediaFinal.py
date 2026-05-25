"""
Exercício 2.3: O sistema de avaliação de determinada disciplina é composto por três
provas. A 1ª prova tem peso 2, a 2ª prova tem peso 3 e a 3ª prova tem peso 5.
Faça um algoritmo para calcular a média final de um aluno desta disciplina.
"""

prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))

media_final = (prova1 * 0.20) + (prova2 * 0.30) + (prova3 * 0.50)

print(f"A média final foi: {media_final}")