# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input('Quanto ganha / hora? '))
numero_de_horas_no_mes = float(input('Número de horas trabalhadas no mês? '))

calc_salario = ganho_por_hora * numero_de_horas_no_mes
print(f'Total de sálario: R$ {round(calc_salario, 2)}')
