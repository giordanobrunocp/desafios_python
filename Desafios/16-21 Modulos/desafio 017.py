from math import sqrt,pow
cat1=int(input('Digite o valor de um cateto: '))
cat2=int(input('Digite o valor do outro cateto: '))
hip= sqrt(pow(cat1,2) + pow(cat2,2))

print('A hipotenusa é {:.2f}'.format(hip))