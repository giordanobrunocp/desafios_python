celsius=float(input('Digite a temperatura em ºC: '))
faih=((celsius * (9/5)) + 32)
kelvin=celsius + 273.15

print('A temperatura {:.2f}ªC equivale a {:.2f}ºF e {:.2f}K'.format(celsius, faih, kelvin))
