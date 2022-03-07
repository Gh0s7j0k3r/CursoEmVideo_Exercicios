'''Faca um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
Se ele ainda vai se alistar ao servico militar.
Se e a hora de se alistar
Se ja passou do tempo de alistamento.
seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
sexo=int(input('Informe qual o seu sexo, sendo 1 para Feminino e 2 para Masculino: '))
if sexo == 2:
    ano=int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        print('Voce tem {} de idade, falta {} anos para o servico militar obrigatorio em {}.'.format(idade,18-idade,date.today().year+(18-idade)))
    elif idade == 18:
        print('Voce possui {} de idade, e hora de se alistar.'.format(idade))
    else:
        print('Voce possui {} de idade, ja passou {} anos que voce deveria ter servido em {}.'.format(idade,idade-18,date.today().year-(idade-18)))
else:
    print('Voce nao precisa se alistar devido ser do sexo Feminino.')