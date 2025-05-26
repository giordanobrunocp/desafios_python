lista = []
pares = []
impares = []
continuar=0

while True:
    num=int(input('Digite um valor: '))
    if num % 2 == 0 and num != 0:
        pares.append(num)
        lista.append(num)
    elif num % 2 == 1 and num != 0:
        impares.append(num)
        lista.append(num)
    else:
        lista.append(num)
    continuar=input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'Dentre os valores {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')