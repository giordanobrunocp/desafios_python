lista=[]

for c in range(1,6):
    peso=float(input('Digite o peso da {}º pessoa: '.format(c)))
    lista.append(peso)
    #print(lista)
print('O maior peso destas pessoas é {}'.format(max(lista)))
print('O menor peso destas pessoas é {}'.format(min(lista)))