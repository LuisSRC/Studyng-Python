#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celcius = float(input('Digite a temperatura em °C: '))
f = (celcius * 1.8) + 32
print(f'A temperatura {celcius}°C convertida para Fahrenheit será de {f}°F')
