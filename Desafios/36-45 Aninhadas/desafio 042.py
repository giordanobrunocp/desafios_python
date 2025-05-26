r1=int(input('Digite o valor da primeira reta: '))
r2=int(input('Digite o valor da segunda reta: '))
r3=int(input('Digite o valor da terceira reta: '))
retas=[r1,r2,r3]
mreta = max(retas)
prova=((r1+r2+r3)-mreta)

if prova > mreta:
    print('Seu triangulo é possível')
    if r1==r2==r3:
        print('Este é um triângulo equilátero')
    elif r1==r2 or r1==r3 or r2==r3:
        print('Este é um triângulo isósceles')
    elif r1!=r2 or r1!=r3 or r2!=r3:
        print('Este é um triângulo escaleno')
else:
    print('Seu triângulo NÃO é possível')

