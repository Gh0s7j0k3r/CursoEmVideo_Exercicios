'''escreva um programa que leia um valor em 
metros e o exiba convertido em centimetros e milimetros'''

metro=float(input('Informe a quantidade de metros: '))
print('Para {} metros informado a quantidade de: \nQuilometros {} \nHectometro {} \nDecametro {} \nDecimetro {:.0f} \nCentimetro {:.0f} \nMilimetros {:.0f}'.format(metro, metro/1000, metro/100, metro/10, metro*10, metro*100, metro*1000))
