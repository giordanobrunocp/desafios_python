dis=int(input('Qual a distância da sua viagem em Kms?\n'))

if dis <= 200:
    print('Sua viagem custará R${:.2f}'.format(dis * 0.50))
else:
    print('Sua viagem custará R${:.2f}'.format(dis * 0.45))