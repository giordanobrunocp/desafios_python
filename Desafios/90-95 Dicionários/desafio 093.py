dados={}

jogador=str(input('Nome do jogador: '))
dados['jogador'] = jogador

partidas=int(input('Quantas partidas: '))
dados['partidas'] = partidas

tgols=0

for c in range(0, partidas):
    gols=int(input(f'Quantos gols na partida {c+1}: '))
    dados[f'partida{c+1}']=gols
    tgols += gols

dados['gols'] = tgols
print(dados)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O total de gols feitos pelo jogador {dados['jogador']} foi {dados['gols']} gols.')