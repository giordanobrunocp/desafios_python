from random import randint
numero=int(input('Digite um número de 1 a 10: '))
pc =int(randint(1,10))
tentativas=1

while numero != pc:
    tentativas+=1
    if numero < pc:
        numero=int(input('O número que estou pensando é maior que {}, tente novamente: '.format(numero)))
    elif numero > pc:
        numero=int(input('O número que estou  pensando é menor que {}, tente novamente: '.format(numero)))


if tentativas == 1:
    print('INCRÍVEL!!!!! você acertou de primeira, o número era {} '.format(numero))
elif tentativas <= 4:
       print('Você acertou em apenas {} tentativas!!! \n O número que eu estava pensando era {}.'.format(tentativas, pc))
elif tentativas > 4:
    print('Você acertou em {} tentativas!\nO número que eu estava pensando era {}.'.format(tentativas,pc))
