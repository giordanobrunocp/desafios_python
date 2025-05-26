continuar = 'S'
total=0
caros=0
item = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preco do produto R$ '))
itembarato=item
precobarato=preco
total += preco
if preco > 1000:
    caros += 1

while continuar == 'S':
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
        item =  str(input('Digite o nome do produto: '))
        preco =  float(input('Digite o preco do produto R$ '))

        total += preco
        if preco > 1000:
            caros+=1
        if preco < precobarato:
            precobarato = preco
            itembarato = item

print(f'O total da compra é de R$ {total:.2f}')
print(f'{caros} produtos custam mais de R$1000 reais')
print(f'O produto mais barato é o {itembarato} e custou R$ {precobarato:.2f}')