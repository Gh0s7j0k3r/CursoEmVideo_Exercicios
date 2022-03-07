'''Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o 
numero solicitado for negativo.'''
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' *30)
    if num < 0:
        break
    for c in range (1,11):
        print(f'{c:2} X {num} = {c*num}')
    print('-'*30)
print('Programa de tabuada encerrado, Volte sempre.')
