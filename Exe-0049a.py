'''Refaca o desafio009, mostrando a tabuada de um numero que o usuario 
escolher, so que agora utilizando um laco for.'''

num=int(input('Digite um numero para a tabuada: '))
escolha=int(input('''Qual tabuada voce deseja?
[1] - Adicao
[2] - Subtracao
[3] - Multiplicacao
[4] - Divisao
Esolha sua opcao: '''))
if escolha >=1 and escolha <=4:
    escolha=escolha
    limite=int(input('Ate qual numero quer a tabuada? '))
    print('\033[1;31m-=\033[m'*6)
    for c in range(1,limite+1):
        if escolha == 1:
            print('{} + {:2} = {}'.format(num,c,c+num))
        elif escolha == 2:
             print('{} - {:2} = {}'.format(num,c,c-num)) 
        elif escolha == 3:
            print('{} x {:2} = {}'.format(num,c,c*num))
        elif escolha == 4:
            print('{} / {:2} = {}'.format(num,c*num,c))
    print('\033[1;31m-=\033[m'*6)
else:
    print('Opcao invalida! Digite novamente!')
