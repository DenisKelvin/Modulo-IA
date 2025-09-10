#calculadora de consumo

#dados da viagem

distancia_percorrida = int(input("Digite a distancia percorrida em km: "))
combustivel_gasto = int(input("Digite o gasto de combustivel em litros: "))

#calculo do consumo

consumo = distancia_percorrida / combustivel_gasto

#exibicao de resultado

print("\nDados da viagem")
print(f"distancia percorrida: {distancia_percorrida} Km")
print(f"combustivel gasto: {combustivel_gasto} em litros")
print(f"consumo medio: {consumo:.2f}")