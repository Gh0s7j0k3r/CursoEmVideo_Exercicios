'''Crie um programa que vai ler varios numeros e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. 
Ao final mostre o conteudo das tres listas geradas.'''

lista = []
while True:
    lista.append(int(input("Digite um numero: ")))
    resp=str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
    