# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

try:
    peso_de_peixes = float(input('Digite o peso de peixes: '))
    if peso_de_peixes <= 0:
        raise Exception('Oops! O peso dos peixes em quilo não pode ser nulo/negativo')
    else:
        if peso_de_peixes > 50:
            excesso = peso_de_peixes - 50
            multa = excesso * 4.00
            print(f'excedeu {round(excesso, 2)} kg')
            print(f'A sua multa é de: R$ {round(multa, 2)}')
        else:
            print(f'João, hoje você não será multado, trouxe {peso_de_peixes} kg')



except ValueError:
    print('Oops! Valores não aceitos')
