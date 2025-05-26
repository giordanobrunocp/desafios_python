matriz = [[], [], []]

for m in range(0,3):
    for c in range(0,3):
        matriz[m].append(int(input(f'Digite um valor para [{m,c}]: ')))

print(matriz[0])
print(matriz[1])
print(matriz[2])