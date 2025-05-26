from datetime import date
ano = date.today().year
total = 0

for c in range(1, 8):
    nasc=int(input('Em que ano nasceu a pessoa {}? '.format(c)))
    idade=ano-nasc
    if idade >=18:
        total += 1
print('Um total de {} pessoas são maiores de idade'.format(total))
print('Um total de {} pessoas são menores de idade'.format(7-total))