peso = float(input("Digite seu peso. "))
altura = float(input("Digite sua altura. "))

imc = peso / (altura * altura)
print(f"Seu imc é: {imc:.2f}")

if imc <= 18.5:
    print("Voce esta abaixo do peso. ")

elif imc > 18.5 and imc <= 25.0:
    print("peso normal. ")

elif imc > 25.0 and imc <= 30.0:
    print("Você esta acima do peso. ")

elif imc <= 0:
    print("Peso invalido. ")

else:
    print("Você esta obeso. ")