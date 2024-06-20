# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (
# (72.7*altura) - 58)

try:
    altura = float(input('Digite a sua altura (h): '))
except ValueError:
    print('Oops, valor não aceito.')
    exit()
calc_peso_ideal = (72.7 * altura) - 58

print(f'O peso ideal: {calc_peso_ideal} Kg')
