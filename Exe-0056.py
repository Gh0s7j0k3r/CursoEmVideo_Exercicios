'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A media de idade do grupo.
Qual e o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.'''

soma=0
cont=0
maioridadehomem=0
fem=0
homem=' '

for c in range (0,4):
    nome=str(input('Informe o nome: ')).strip()
    idade=int(input('Idade: '))
    print('Informe seu sexo\nDigite\n[1] - Feminino\n[2] - Masculino')
    sexo=int(input('Opcao: '))
    soma += idade
    cont += c
    if c == 0 and sexo == 2:
        maioridadehomem= idade
        homem=nome
    if sexo == 2 and idade > maioridadehomem:
        maioridadehomem=idade
        homem=nome
    if sexo == 1 and idade < 20:
        fem += 1
media=int(soma/cont)
print('A media de idade e: {}\nO homem mais velho tem {} anos, e seu nome e {}.\n{} mulheres tem menos de 20 anos.'.format(media,maioridadehomem,homem,fem))
