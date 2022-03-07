'''Crie um programa que leia varios numeros inteiros pelo teclado. O 
programa so vai parar quando o usuario digitar o valor 999, que e a 
condicao de parada. No final mostre quantos numeros foram digitados e 
qual foi a soma entre eles, (desconsiderando o flag).'''

numero=0
cont=0
soma=0
numero=int(input('Digite um numero [999 para parar]: '))
while numero != 999:
    cont += 1
    soma += numero
    numero=int(input('Digite um numero [999 para parar]: '))
print('Foram digitados {} numero e a soma entre todos os numeros e {}'.format(cont, soma))
