tudo=[]
dados=[]
while True:
    dados.append(float(input('Peso: ')))
    dados.append(str(input('Nome: ')))
    tudo.append(dados[:])
    dados.clear()
    continuar=input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastras {len(tudo)} pessoas.')
tudo.sort()
print(f'Os mais leves: {tudo}')
tudo.sort(reverse=True)
print(f'Os mais pesados: {tudo}')
