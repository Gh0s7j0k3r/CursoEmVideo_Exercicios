'''Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso mostre:
A-Quantos numeros foram digitados.
B-A lista de valores ordenada de forma decrescente.
C-Se o valor 5 foi digitado e está ou não na lista. '''

valores = []
while True:
    valores.append(int(input('Digite um numero: ')))
    resposta = str(input('Deseja continuar? S/N '))
    if resposta in "nN":
        break
print(f"Foram digitados {len(valores)} numeros.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print(f"O numero 5 consta na lista.")
else:
    print("Não foi encontrado o numero 5 na lista.")
