lista = []

for c in range(0, 5):
    lista.append(int(input('Insira um número: ')))

maior = max(lista)
menor = min(lista)

print(f'\nO maior número digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} ', end='')

print(f'\nO menor número digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i} ', end='')
