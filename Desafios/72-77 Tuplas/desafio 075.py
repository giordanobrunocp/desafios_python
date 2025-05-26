n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite outro número: '))
n4=int(input('Digite outro número: '))
tupla=(n1,n2,n3,n4)

print(tupla)
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3)}')
else:
    print('O número 3 não apareceu na tupla')
    print('Os números pares desta tupla são: ', end='')
for n in tupla:
    if n % 2 == 0 and n != 0:
        print(n, end=' ')