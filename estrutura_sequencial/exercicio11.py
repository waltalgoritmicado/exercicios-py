# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

try:
    iNum1 = int(input(''))
    iNum2 = int(input(''))
    fNum = float(input(''))
except ValueError:
    print('Oops! Valor não aceito.')
    exit()

command1 = iNum2 / 2
command2 = iNum1 * 3 + fNum
command3 = fNum ** 3
print(f'o produto do dobro do primeiro com metade do segundo: {command1}')
print(f'a soma do triplo do primeiro com o terceiro: {command2}')
print(f'o terceiro elevado ao cubo: {command3}')
