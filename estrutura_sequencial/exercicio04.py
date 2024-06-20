# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('primeiro bimestre: '))
nota2 = float(input('segundo bimestre: '))
nota3 = float(input('terceiro bimestre: '))
nota4 = float(input('quarto bimestre:é '))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print(f'Média: {round(media, 3)}')
