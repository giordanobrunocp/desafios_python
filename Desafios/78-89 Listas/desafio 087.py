matriz = [[], [], []]
pares=0
col=0
linha=0

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l,c}]: ')))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            col += matriz[l][c]
        if l == 1:
            linha += matriz[l][c]

print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'Soma dos pares: {pares}')
print(f'A soma da terceira coluna: {col}')
print(f'O maior valor da segunda linha: {linha}')