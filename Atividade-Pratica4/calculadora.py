operador = input("Digite um operador: +, -, *, /: ")
if operador not in ['+', '-', '*', '/' ]:
    print("Operador invalido, escolha um dos mostrados acima! ")
else:
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        if operador == '+':
            resultado = num1 + num2
            print(f"O resultado é {resultado:.2f}")
            
        elif operador == '-':
            resultado = num1 - num2
            print(f"O resultado é {resultado:.2f}")

        elif operador == '*':
            resultado = num1 * num2
            print(f"O resultado é {resultado:.2f}")

        elif operador == '/':
            try:
                resultado = num1 / num2
                print(f"O resultado é {resultado:.2f}")
            except ZeroDivisionError:
                print("Impossivel dividir por zero! ")
    
    except ValueError:
        print("Digite apenas numeros! ")



