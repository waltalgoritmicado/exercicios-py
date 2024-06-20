# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

try:
    t_em_graus_fahrenheit = int(input('Digite a temperatura em graus Fahrenheit: '))
except ValueError:
    print('Oops! Valor não aceito')
    exit()


C = 5 * ((t_em_graus_fahrenheit-32) / 9)
print(f'{round(C, 2)}')
