'''Escreva um programa que leia um numero inteiro qualquer e peca para 
o usuario escolher qual sera a base de conversao:
1 para binario, 2 para octal, 3 para hexadecimal'''

num=int(input('Digite um numero inteiro: '))
escolha=int(input('Para converter o numero {} para binario, octal ou hexadecimal digite:\n1 - Binario\n2 - Octal\n3 - Hexadecimal\nPara qual base deseja converter? '))
if escolha == 1:
    conversao = bin(num)[2:]
elif escolha == 2:
    conversao = oct(num)[2:]
elif escolha == 3:
    conversao = hex(num)[2:]
else:
    print('Numero invalido!')
print('O numero {} convertido para a base {} e {}.'.format(num,escolha,conversao))
