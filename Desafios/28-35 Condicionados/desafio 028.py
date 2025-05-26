from random import randint
n=randint(1,5)

t1=int(input('Chute um número entre 1 e 5: '))

if t1 == n:
    print('Você acertou!!!')
else:
    print('Você errou...')
print('O número era {}'.format(n))