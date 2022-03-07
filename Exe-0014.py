'''Escreva um programa que converta uma temperatura digitada em 
graus Celsius e converta para graus Fahrenheit'''

temp=float(input('Informe a temperatura em Celsius: '))
far=(temp*9/5)+32
print('A temperatura {:.1f} em Celsius, a mesma em Fahrenheit passa a ser {:.1f}'.format(temp,far))
