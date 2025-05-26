r1=int(input('Digite o valor da primeira reta: '))
r2=int(input('Digite o valor da segunda reta: '))
r3=int(input('Digite o valor da terceira reta: '))
retas=[r1,r2,r3]
mreta = max(retas)
prova=((r1+r2+r3)-mreta)

if prova > mreta:
    print('Seu triangulo é possível')
else:
    print('Seu triângulo não é possível')


print('Reta 1','\033[0;33;42m \033[m'*r1)
print('Reta 2','\033[0;33;41m \033[m'*r2)
print('Reta 3','\033[0;33;44m \033[m'*r3)