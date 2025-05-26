'''from random import randint
dados={}

for c in range(1,5):
    dados[f'jogador{c}']= (randint(1, 6))
    print(f'O jogador {c} tirou {dados[f'jogador{c}']} no dado.')

if dados['jogador1'] >= dados['jogador2'] and dados['jogador1'] >= dados['jogador3'] and dados['jogador1'] >= dados['jogador4']:
    print('O jogador 1 venceu.')
if dados['jogador2'] >= dados['jogador1'] and dados['jogador2'] >= dados['jogador3'] and dados['jogador2'] >= dados['jogador4']:
    print('O jogador 2 venceu.')
if dados['jogador3'] >= dados['jogador1'] and dados['jogador3'] >= dados['jogador2'] and dados['jogador3'] >= dados['jogador4']:
    print('O jogador 3 venceu.')
if dados['jogador4'] >= dados['jogador1'] and dados['jogador4'] >= dados['jogador3'] and dados['jogador4'] >= dados['jogador2']:
    print('O jogador 4 venceu.')'''

from random import randint
from operator import itemgetter
dados={}
for c in range(1,5):
    dados[f'jogador{c}']= (randint(1, 6))
    print(f'O jogador {c} tirou {dados[f'jogador{c}']} no dado.')
ranking = list()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')