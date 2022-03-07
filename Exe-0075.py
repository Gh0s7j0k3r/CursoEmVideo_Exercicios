'''Desenvolva um programa que leia quartro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A- Quantas vezes apareceu o valor 9.
B- Em que posicao foi digitado o primeiro valor 3.
C- Quais foram os numeros pares. '''

numero=(int(input('Digite um numero: ')),int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
