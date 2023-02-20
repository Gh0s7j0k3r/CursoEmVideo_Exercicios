'''Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). 
No final, mostre a lista ordenada na tela. '''
'''
cont=0
valores = []
for c in range (0, 5):
    num=int(input('Digite um valor: '))
    while len(valores) <=5:
        if num <= valores[cont]:
            valores.insert[num, cont+1]
    
print(len(valores))
print(f"Os valores digitados foram {valores}")'''

lista = []
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')