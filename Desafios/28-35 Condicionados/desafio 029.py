vel=float(input('Qual a velocidade do carro em km/h? '))
if vel <= 80:
    print('Você está dentro do limite de velocidade de 80km/h.')
else:
    print('Você será multado, sua multa é de R${:.2f}' .format((vel-80)*7))