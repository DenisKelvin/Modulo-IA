def verificador_de_senhas():
    while True:
        senha = input("Digite sua senha ou sair para finalizar. ").lower()
        
        if senha == 'sair':
            print("Programa Finalizado. ")
            break

        if len(senha) < 8:
            print("Por maior segurança digite uma senha com no minimo 8 caracteres! ")
            continue

        if not any(letra.isdigit() for letra in senha):
            print("Digite no minimo um numero! ")
            continue

        print("Senha forte e valida! ")
        break

verificador_de_senhas()
