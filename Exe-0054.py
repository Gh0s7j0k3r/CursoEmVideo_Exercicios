'''Crie um program que leia o ano de nascimento de sete pessoas. No final
mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao 
maiores.'''

from datetime import date
cont=0
cont1=0
for c in range(0,7):
    ano=int(input('Ano de nascimento: '))
    idade=date.today().year - ano
    if idade >= 18:
        cont=cont+1
    else:
        cont1=cont1+1
print('{} pessoas tem mais de 18 anos.'.format(cont))
print('{} pessoas tem menos de 18 anos.'.format(cont1))
