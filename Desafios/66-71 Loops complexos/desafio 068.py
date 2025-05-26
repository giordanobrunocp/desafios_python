#Par ou impar
from random import randint
placar=0

while True:
    print(20 * '==')
    escolhido = str(input('Você quer Par ou Impar? [P/I]: ')).strip().upper()[0]

    if escolhido not in ('P','I'):
        print('Opção inválida, tente novamente.')
        continue

    pc=randint(1,5)
    jogado=int(input('Digite um número de 0 a 5: '))
    soma=pc+jogado
    if jogado >5:
        print('Número inválido, tente novamente.')
        continue

    print(f'O computador jogou {pc} e a soma deu {soma} que é ', end='')
    if soma % 2 == 0:
        print('Par')
        if escolhido == 'P':
            print('Você venceu!')
            placar +=1
            print(f'Você ganhou {placar} vezes')
        else:
            break
    else:
        print('Ímpar')
        if escolhido == 'I':
            print('Você venceu!')
            placar += 1
            print(f'Você ganhou {placar} vezes')
        else:
            break
print(f'Você perdeu...Você ganhou {placar} vezes \nEncerrando jogo...')
