'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa
Seu programa devera realizar a operacao solicitada em cada caso.'''

from time import sleep

valor1=int(input('Primeiro valor: '))
valor2=int(input('Segundo valor: '))
escolha=0
while escolha != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa')
    escolha=int(input('>>>>> Qual a sua opcao? '))
    if escolha == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} e igual a {}.'.format(valor1,valor2,soma))
    elif escolha == 2:
        mult = valor1 * valor2
        print('A multiplicacao entre {} x {} e igual a {}.'.format(valor1,valor2,mult))
    elif escolha == 3:
        if valor1 > valor2:
            maior = valor1
            print('Entre {} e {} o maior valor e {}.'.format(valor1,valor2,maior))
        elif valor2 > valor1:
            maior = valor2
            print('Entre {} e {} o maior valor e {}.'.format(valor2,valor1,maior))
        else:
            print('Os valores sao iguais.')
    elif escolha == 4:
        valor1=int(input('Primeiro valor: '))
        valor2=int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando o programa!')
        sleep(2)
    else:
        print('Opcao invalida! tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fim do programa, volte sempre!')
