def calculador(preço, percentual_desconto):
    desconto = preço * (percentual_desconto / 100)
    preço_final = preço - desconto
    return preço_final

preço_original = float(input("Digite o preço do produto!: R$"))
desconto = float(input("Digite o valor do desconto!: "))

total = calculador(preço_original, desconto)
print(f"Valor do produto: {preço_original:.2f}")
print(f"Valor do desconto: {desconto:.2f}")
print(f"Valor total:{total:.2f}")
