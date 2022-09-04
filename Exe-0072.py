'''Crie um programa que ternha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso. '''

contagem = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    numero=int(input('Digite um numero entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        print(f'Voce digitou o numero {contagem[numero]}')
        opcao=' '
        while opcao not in 'SN':
            opcao=str(input('Deseja continuar? [S/N]')).strip().upper()
        if opcao == 'N':
            break
    else:
        print('Tente novamente!')
            