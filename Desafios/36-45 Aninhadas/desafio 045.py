from random import choice

jogada=str(input('Qual a sua jogada? Pedra, Papel ou Tesoura? ')).strip().lower()
pc=choice(['pedra', 'papel', 'tesoura'])

print('O Computador joga {}'.format(pc))
if jogada==pc:
    print('EMPATE')
elif ((jogada=='pedra' and pc=='tesoura') or (jogada=='papel' and pc=='pedra')):
    print('VOCÊ VENCEU!!!')
elif ((jogada=='papel' and pc=='tesoura') or (jogada=='pedra' and pc=='papel')):
    print('Você perdeu...')