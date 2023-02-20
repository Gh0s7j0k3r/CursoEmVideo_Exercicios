'''Crie um programa que vai ler varios numeros e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. 
Ao final mostre o conteudo das tres listas geradas.'''

lista = []
par = []
impar = []
while True:
    lista.append(int(input("Digite um numero: ")))
    resp=str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for c in range (0, len(lista)): #for i, v in enumerate(lista):
    divisao = lista[c] % 2 #Não existiu essa linha
    if divisao == 0: # if v % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(f'Foram digitados os numeros: {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de pares é {impar}')
