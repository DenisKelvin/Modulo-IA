def calculador_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_da_conta = float(input("digite o valor total da sua conta do restaurante: "))
porcentagem = float(input("Quantos porcentos % voce deseja pagar de gorjeta: "))
gorjeta = calculador_gorjeta(total_da_conta, porcentagem)
print(f"Para uma conta de R${total_da_conta}, voce deseja pagar {porcentagem}% de gorjeta - R${gorjeta:.2f}")

