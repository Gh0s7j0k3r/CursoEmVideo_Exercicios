'''Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. 
Caso o numero já exista lá dentro, ele não sera adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente. '''

valores = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        print('Valor adicionado com sucesso...')
        valores.append(num)
    else:
        print('Valor duplicado! Não vou adicionar...')
    decisao = str(input('Quer continuar? [S/N]')).strip().upper()
    if decisao == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
