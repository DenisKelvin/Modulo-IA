idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Você é criança. ")
elif idade >= 13 and idade <= 17:
    print("Você é adolescente. ")
elif idade >= 18 and idade <= 59:
    print("Você é adulto. ")
elif idade < 0:
    print("Idade invalida. ")    
else:
    print("Você é idoso. ")

