import requests
import json

URL_API = "https://jsonplaceholder.typicode.com/users"

def coleta_d_usuarios():
    print("Coletando usuarios da API...")
    try:
        response = requests.get(URL_API)
        if response.status_code == 200:
            usuarios = response.json()

            salvar_usuarios(usuarios, "usuarios.json")
            print("coleta concluida com sucesso! Os dados foram salvos em 'usuarios.json'.")
        else:
            print(f"Erro na requisição: Status Code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar á api: {e}")

def salvar_usuarios(data, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4,ensure_ascii=False)

if __name__ == "__main__":
    coleta_d_usuarios()        





    