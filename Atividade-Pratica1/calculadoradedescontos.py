#Calculadora de desconto
nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
porcentagem_de_desconto = int(input("Digite o valor do cupom promocional: "))

#calculo do desconto e preço final

valor_desconto = valor_produto * (porcentagem_de_desconto / 100)
preco_final = valor_produto - valor_desconto

#exibicao dos resultados
print(f"produto: {nome_produto}")
print(f"valor do produto: {valor_produto:.2f}")
print(f"cupom de desconto: {porcentagem_de_desconto:.2f}")
print(f"Valor do cupom: {valor_desconto:.2f}")
print(f"Preco final: {preco_final:.2f}")
