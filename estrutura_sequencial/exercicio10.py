# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

try:
    t_em_graus_celsius = input('Digite a temperatura em graus celsius: ')
except ValueError:
    print('Oops! Valor não aceito.')
    exit()

F = float(t_em_graus_celsius) * 1.8 + 32

print(f'{F}')
