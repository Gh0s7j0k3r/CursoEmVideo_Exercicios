'''Crie um programa que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final, de acordo com a media atingida:
Media abaixo de 5.0: Reprovado
Media entre 5.0 e 6.9: Recuperacao
Media 7.0 ou superior: Aprovado'''

nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
media=(nota1+nota2)/2
reprovado=5
recuperacao=6.9
aprovado=7
if media < reprovado:
    print('Sua media e {} e a mesma ficou abaixo de 5, desta forma voce esta \033[1;4;31mReprovado!\033[m'.format(media))
elif media <= recuperacao:
    print('Sua media e {} e a mesma ficou abaixo de 7, desta forma voce esta de \033[1;4;33mRecuperacao!\033[m'.format(media))
else:
    print('Sua media e {}, voce foi \033[1;4;32mAprovado!\033[m'.format(media))
