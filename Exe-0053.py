'''Crie um programa que leia uma frase qualquer e diga se ela e um 
palindromo, desconsiderando os espacos.
EX:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''

frase=str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto=''.join(palavras)
inverso=''
#inverso=junto[::-1]
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} e {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')