from random import randint
from time import sleep

def sorteia():
    numeros = []
    for _ in range(5):
        n = randint(0, 9)
        numeros.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print()
    return numeros

def somapar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


# Programa principal
print('Números sorteados:')
somapar(sorteia())
