#notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#calculo das notas
media = (nota1 + nota2 + nota3) / 3

#exibicao de resultados

print(f"notas do aluno")
print(f"nota1: {nota1}")
print(f"nota2: {nota2}")
print(f"nota3: {nota3}")
print(f"A media é: {media:.2f}")