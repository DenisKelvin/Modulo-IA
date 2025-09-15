def verif_palindromo(texto):
    texto_limpo = ''. join(letra.lower() for letra in texto if letra.isalnum())

    return texto_limpo == texto_limpo[::-1]

frase = input("digite uma frase ou palavra: ")
resultado = verif_palindromo(frase)

if resultado == True:
    resposta = 'Sim'

else:
    resposta = 'Não'

print(f"{frase} é um palindromo? {resposta}")