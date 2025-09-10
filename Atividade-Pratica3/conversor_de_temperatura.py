celsius = float(input("digite a temperatura em celsius: "))
kelvin = float(input("digite a temperatura em kelvin: "))
fahrenheit = float(input("digite a temperatura em fahrenheit: "))

celsius_para_kelvin = celsius + kelvin
celsius_para_fahrenheit = (celsius * 1.8) + 32
kelvin_para_fahrenheit = (kelvin - 273.15 * 1.8) + 32
kelvin_para_celsius = kelvin - 273.15
fahrenheit_para_celsius = (fahrenheit - 32) / 1.8
fahrenheit_para_kelvin = (fahrenheit - 32 / 1.8) + kelvin

print(f"Temperatura em celsius: {celsius}")
print(f"Temperatura em kelvin: {kelvin}")
print(f"Temperatura em fahrenheit: {fahrenheit}")
print(f"O resultado de celsius para kelvin: {celsius_para_kelvin:.2f}")
print(f"O resultado de celsius para fahrenheit: {celsius_para_fahrenheit:.2f}")
print(f"O resultado de kelvin para celsius: {kelvin_para_celsius:.2f}")
print(f"O resultado de kelvin para fahrenheit: {kelvin_para_fahrenheit:.2f}")
print(f"O resultado de fahrenheit para celsius: {fahrenheit_para_celsius:.2f} ")
print(f"O resultado de fahrenheit para kelvin: {fahrenheit_para_kelvin:.2f}")
