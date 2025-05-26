from random import randint
sorteio=[]

dezenas=int(input('Digite quantas dezenas você deseja:'  ))
for d in range(0,dezenas):
    sort=[]
    for n in range(0,6):
        num=randint(1,60)
        while num in sorteio:
            num=randint(1,60)
        sort.append(num)
        sort.sort()
    sorteio.append(sort)
print(sorteio, end='\n')
