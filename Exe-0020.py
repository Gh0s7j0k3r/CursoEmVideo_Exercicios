'''O mesmo professor do desafio anterior quer sortear a ordem de 
apresentacao de trabalhos dos alunos. Faca um programa que leia o nome
 dos quatro alunos e mostre a ordem sorteada.'''
 
from random import shuffle

PrimeiroAluno=str(input('Primeiro Aluno: '))
SegundoAluno=str(input('Segundo Aluno: '))
TerceiroAluno=str(input('Terceiro Aluno: '))
QuartoAluno=str(input('Quarto Aluno: '))
lista=[PrimeiroAluno,SegundoAluno,TerceiroAluno,QuartoAluno]
shuffle(lista)
print('A ordem de apresentacao sera: {}'.format(lista))
