import pandas as pd

def processar_logs(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execuçao'].mean()
    desvio_padrão = df['tempo_execuçao'].std()
    print(f"Tempo de Execuçao:\nMedia: {media_tempo:.2f}\nDesvioPadrao: {DesvioPadrao:2f}")

arquivo = input("Digite o nome do arquivo: ").strip()
processar_logs(arquivo)    
