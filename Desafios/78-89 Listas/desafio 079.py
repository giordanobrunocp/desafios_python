lista=[]
while True:
    num=int(input(('Insira um número: ')))
    continuar=input('Deseja continuar? [S/N] ').upper().strip()[0]
    if num not in lista:
        lista.append(num)
    if continuar=='N':
        break
print(f'Números digitados: {sorted(lista)}')