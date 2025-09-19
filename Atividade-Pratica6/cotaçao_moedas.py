import requests

def obter_cotaçao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()[moeda + 'BRL']
    return f"Moeda: {moeda}/BRL\nValor: R${dados['bid']}\nMaximo: R$R${dados['high']}\nMinimo: R$R${dados['low']}\nAtualizaçao: {dados['create_date']}"

moeda = input("Digite o codigo da moeda (USD, EUR): ")
print(obter_cotaçao(moeda))    