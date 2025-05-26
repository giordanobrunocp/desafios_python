num=str(input('Digite um numero de 0 a 9999: '))
num = num.zfill(4)

print('Milhar {}'.format (num[0]))
print('Centena {}'.format(num[1]))
print('Dezena {}'.format(num[2]))
print('Unidade {}' .format(num[3]))