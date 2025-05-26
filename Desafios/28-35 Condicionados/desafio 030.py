n=int(input('Digite um número inteiro positivo: '))
np=n%2

if np==0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))