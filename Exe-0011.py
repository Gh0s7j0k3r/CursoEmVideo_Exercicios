'''faca um programa que leia a largura e a altura de uma parede em
metros, calcule a sua area e a quantidade de tinta necessaria 
para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2'''

largura=float(input('Informe a largura da parede em metros: '))
altura=float(input('Informe a Altura da parede em metros: '))
m2=largura*altura
print('E necessario {}l de tinta para pintar {}m2 de parede.'.format(m2/2,m2))
