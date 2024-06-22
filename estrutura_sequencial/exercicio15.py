# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

try:
    ganho_por_hora = float(input('Quanto ganha por hora? '))
    n_de_horas_trabalhadas = int(input('Quanto em horas trabalhou no mês? '))
    calc_salario_mensal = round(ganho_por_hora * n_de_horas_trabalhadas, 2)

    if calc_salario_mensal <= 0.00:
        print('O seu salário não pode ser nulo/negativo')
    else:
        salario_bruto = calc_salario_mensal
        pago_irr = salario_bruto * 0.11
        pago_inss = salario_bruto * 0.08
        pago_sindicato = salario_bruto * 0.05
        descontos = pago_irr + pago_inss + pago_sindicato
        salario_liquido = salario_bruto - descontos

        print(f'Salário Bruto : R$ {calc_salario_mensal}')
        print(f'IR (11%) : R$ {pago_irr}')
        print(f'INSS (8%) : R$ {pago_inss}')
        print(f'Sindicato (5%) : R$ {pago_sindicato}')
        print(f'Salário Liquido : R$ {salario_liquido}')


except ValueError:
    print('Oops, ERROR')
