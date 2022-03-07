'''A confederacao nacional de natacao precisa de um programa que leia o 
ano de nascimento de um atleta e mostre sua categoria, de acordo com a 
idade:
Ate 9 anos: Mirim
Ate 14 anos: Infantil
Ate 19 anos: Junior
Ate 20 anos: Senior
Acima: Master'''

from datetime import date
ano=int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano 
if idade <= 9:
    categoria = 'Mirim'
elif idade >9 and idade <= 14:
    categoria = 'Infantil'
elif idade >14 and idade <= 19:
    categoria = 'Junior'
elif idade >19 and idade ==20:
    categoria = 'Senior'
else:
    categoria = 'Master'
print('Voce nasceu no ano {}, com isso sua idade e {} e sua categoria e: {}.'.format(ano,idade,categoria))