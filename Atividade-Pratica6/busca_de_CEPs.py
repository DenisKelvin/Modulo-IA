import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    return f"cep: {dados['cep']}\nRua: {dados['logradouro']}\nBairro: {dados['bairro']}\nCidade: {dados['localidade']}\nEstado: {dados['uf']}"

cep = input("Digite seu cep: ")
print(consultar_cep(cep))