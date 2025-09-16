import random

def gerador_d_senhas():
    letras_min = 'abcdefghijklmnopqrstuvmxyz'
    letras_maius = 'ABCDEFGHIJKLMNOPQRSTUVMXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+'

    todos_caracteres = letras_min + letras_maius + numeros + simbolos
    tamanho_da_senha = int(input('Qual o tamanho da senha que voçê quer? '))

    senha = ''
    for _ in range(tamanho_da_senha):
        senha += random.choice(todos_caracteres)
    
    print(f"Sua genha gerada é: {senha}")

gerador_d_senhas()    


