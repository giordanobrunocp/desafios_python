n1= int(input('Digite um número inteiro: '))
n2= int(input('Digite outro número inteiro: '))
n3= int(input('Digite outro número inteiro: '))

'''if ((n1 or n2) > n3):
    if n1 > n2:
        print('O número {} é maior'.format(n1))
    else:
        print('O número {} é o maior'.format(n2))
else:
    print('O {} é o maior número digitado'.format(n3))'''

maior = max(n1, n2, n3)
minimo = min(n1, n2, n3)
print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(minimo))
