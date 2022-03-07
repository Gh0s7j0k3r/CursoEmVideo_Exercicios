'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada
pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao
continuar. No final, mostre:
A-Quantas pessoas tem mais de 18 anos.
B-Quantos homens foram cadastrados.
C-Quantas mulheres tem menos de 20 anos.'''

quant=homem=mulher=0
while True:
    print('-'*20)
    print('Cadastre uma Pessoa')
    print('-'*20)
    idade=int(input('Idade: '))
    if idade >= 18:
        quant += 1
    sexo=" "
    while sexo not in 'MF':
        sexo=str(input('[M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {quant}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
