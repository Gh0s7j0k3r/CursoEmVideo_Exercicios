'''Refaca o desafio009, mostrando a tabuada de um numero que o usuario 
escolher, so que agora utilizando um laco for.'''

num=int(input('Informe um numero para a tabuada: '))
print('\033[1;34m-=\033[m'*6)
for c in range (1,11):
    print('{:2} x {} = {}'.format(c,num,c*num))
print('\033[1;34m-=\033[m'*6)