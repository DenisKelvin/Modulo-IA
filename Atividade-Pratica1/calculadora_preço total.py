nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o valor unitario do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

preco_total = preco_unitario * quantidade

print(f"Produto: {nome_produto}")
print(f"Preco unitario: R$ {preco_unitario: .2f}")
print(f"Quantidade: {quantidade: .2f}")
print(f"Total: R$ {preco_total: .2f}")

print(preco_total)
