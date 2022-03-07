'''Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. no final,
mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)'''
c = s = 0
while True:
    n = int(input('Digite um valor: (999 para parar) '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}!')