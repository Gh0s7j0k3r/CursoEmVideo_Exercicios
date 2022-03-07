'''desenvolva um programa que leia as duas notas de um 
aluno, calcule e mostre a sua media'''

nota1=float(input('Informe sua primeira nota: '))
nota2=float(input('Informe sua segunda nota: '))
print('A media entre {:.1f} e {:.1f} e igual a {:.1f}'.format(nota1,nota2,(nota1+nota2)/2))