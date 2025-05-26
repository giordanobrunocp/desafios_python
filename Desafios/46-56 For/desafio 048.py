soma=0
num=0
for c in range(0, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        num += 1
print (soma)
print('Foram somados {} números'.format(num))
