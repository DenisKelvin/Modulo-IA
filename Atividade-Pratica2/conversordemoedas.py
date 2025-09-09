#conversor de moedas para dolar e euro

#Valor das moedas
valor_em_reais = float(input("Digite o valor em reais: "))
cotacao_dolar = 5.20
cotacao_euro = 6.15

#conversao
conversao_em_dolar = valor_em_reais / cotacao_dolar
conversao_em_euro = valor_em_reais / cotacao_euro

#exibiçao ods resultados
print(f"Saldo em reais: {valor_em_reais: .2f}")
print(f"O resultado da conversao em dolares é {conversao_em_dolar: .2f}")
print(f"O resultado da conversao em euro é {conversao_em_euro: .2f}")
