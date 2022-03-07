'''Faca um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra "A".
Em que posicao ela aparece a primeira vez.
Em que posicao ela aparece a ultima vez.'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes, a primeira na posicao {} e a ultima aparece em {}.'.format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))
