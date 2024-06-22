# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

try:
    altura = float(input('Digite a altura: '))
    calc_peso_ideal_para_homem = 72.7 * altura - 58
    calc_peso_ideal_para_mulher = 62.1 * altura - 44.7
    print(f'O peso ideal para homens é: {round(calc_peso_ideal_para_homem, 2)} kg')
    print(f'O peso ideal para mulheres é: {round(calc_peso_ideal_para_mulher, 2)} kg')
except ValueError:
    print('Oops! Valor não aceito.')

