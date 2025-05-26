nums = [[],[],[]]
for c in range(0, 7):
    dado=int((input(f'Digite o {c+1}º valor: ')))
    if dado % 2==0 and dado != 0:
        nums[0].append(dado)
    elif dado%2==1:
        nums[1].append(dado)
    else:
        nums[2].append(dado)

nums[0].sort
nums[1].sort
print(f'Números pares: {nums[0]}\nNúmeros ímpares: {nums[1]} \nZeros: {nums[2]}')
