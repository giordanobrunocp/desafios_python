from time import sleep

def linha():
    print()
    print('~' * 30)

def contador(a, b, c):
    linha()
    if c == 0:
        c = 1
    if a > b and c > 0:
        c = -c
    if c < 0:
        c = +c

    for x in range(a, b + (1 if c > 0 else -1), c):
        print(x, end=' ', flush=True)
        sleep(0.3)
    print()


a = int(input('Digite o primeiro termo: '))
b = int(input('Digite o último termo: '))
c = int(input('Digite a razão: '))

contador(1, 10, 1)
contador(10, 0 , 2)
contador(a, b, c)
