'''Crie um programa que leia o nome de uma cidade e diga se ela
comeca ou nao com o nome "SANTO"'''

cidade=str(input('Informe o nome da cidade: ')).strip().capitalize().split()
print('Santo' in cidade[0])
