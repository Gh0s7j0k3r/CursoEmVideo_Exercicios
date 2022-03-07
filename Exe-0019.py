'''Um professor quer sortear um dos seus quatro alunos para apagar
 o quadro. Faca um programa que ajude ele, lendo o nome deles
  e escrevendo o nome do escolhido.'''

from random import choice

PrimeiroAluno=input('Primeiro Aluno: ')
SegundoAluno=input('Segundo Aluno: ')
TerceiroAluno=input('Terceiro Aluno: ')
QuartoAluno=input('Quarto Aluno: ')
print('O Aluno escolhido foi {}'.format(choice([PrimeiroAluno, SegundoAluno,TerceiroAluno,QuartoAluno])))
