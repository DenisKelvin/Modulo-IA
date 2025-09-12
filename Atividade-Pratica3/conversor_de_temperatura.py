while True:
    conversor = input("Escolha um convertor: (cpk, cpf, kpc, kpf, fpc, fpk, sair )").lower()
    if conversor == 'sair':
        print("Encerrando! ")
        break
    
    if conversor not in ['cpk', 'cpf', 'kpc', 'kpf', 'fpc', 'fpk', 'sair' ]:
        print("Escolha um dos mostrados acima! ")
        continue
    
    try:
        num1 = float(input("informe o clima que deseja converter: "))
        
        if conversor == 'cpk':
            calculo = num1 + 273.15
            print(f"O resultado é {calculo:.2f}")

        elif conversor == 'cpf':
            calculo = (num1 * 1.8) + 32
            print(f"O resultado é {calculo:.2f}")
            
        elif conversor == 'kpc':
            calculo = num1 - 273.15
            print(f"O resultado é {calculo:.2f}") 
            
        elif conversor == 'kpf':
            calculo = (num1 - 273.15 * 1.8) + 32
            print(f"O resultado é {calculo:.2f}")
            
        elif conversor == 'fpc':
            calculo = (num1 - 32) / 1.8
            print(f"O resultado é {calculo:.2f}")
            
        elif conversor == 'fpk':
            calculo = (num1 - 32 / 1.8) + 273.15
            print(f"O resultado é {calculo:.2f}")   

    except ValueError:
        print("Digite apenas numeros! ")    
