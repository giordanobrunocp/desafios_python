lista=[]

while True:
    num=int(input('Digite um número: '))
    lista.append(num)
    continuar=input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar=='N':
        break

print(f'\nForam digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os números digitados em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está na lista')