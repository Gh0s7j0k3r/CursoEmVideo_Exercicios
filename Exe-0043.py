'''Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 ate 30: Sobrepeso
30 ate 40: Obesidade
Acima de 40: Obesidade morbida'''

peso=float(input('Informe seu peso: '))
altura=float(input('Informe sua altura: '))
imc=peso/pow(altura,2)
if imc < 18.5:
    grau = 'abaixo do peso.'
elif imc >=18.5 and imc <25:
    grau = 'com peso ideal.'
elif imc >=25 and imc <30:
    grau = 'com sobrepeso.'
elif imc >=30 and imc <40:
    grau = 'com obesidade.'
else:
    grau = 'com obesidade morbida.'
print('Para o peso {:.2f} e altura {:.2f}, o seu imc e {:.1f} e esta {}'.format(peso, altura, imc, grau))
