def contador(*num):
    print(f'Foram digitados {len(num)} números')
    print(f'O maior deles foi {max(num)}')

nums=[]
while True:
    n=(int(input('Digite um número [999 para parar]: ')))
    if n == 999:
        break
    nums.append(n)
contador(*nums)


