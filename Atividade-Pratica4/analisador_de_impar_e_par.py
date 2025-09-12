def analisador_de_num():
    numeros_pares = 0
    numeros_impares = 0

    while True:
        entrada = input("Digite um numero inteiro ou sair para encerrar. ")
        
        if entrada == 'sair':
            print("Encerrado. ")
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O numero {numero} é par.")
                numeros_pares += 1
            else:
                numeros_impares += 1
                print(f"O numero {numero} é impar. ")

        except ValueError:
            print("Entrada invalida. Digite um numero inteiro! ")
            continue
        
        print(f"\nResultado")
        print(f"Total de numeros pares {numeros_pares}")
        print(f"Total de numeros pares {numeros_impares}")

analisador_de_num()        


