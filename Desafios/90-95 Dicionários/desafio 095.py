time={}

while True:
    dados = {}
    gols = []
    jogador=str(input('Nome do jogador: ')).strip().title()
    if jogador == '':
        break
    dados['jogador'] = jogador

    partidas=int(input('Quantas partidas: '))
    dados['partidas'] = partidas

    for c in range(0, partidas):
        gol=int(input(f'Quantos gols na partida {c+1}: '))
        gols.append(gol)
        dados['gols'] = gols
        dados['total'] = sum(gols)
    time[jogador] = dados.copy()

print(time)
print('      Jogador            Gols         Total')
for nome, dados in time.items():
    print(f'{nome:.<20}{dados["gols"]}{dados["total"]:.>10}')

while True:
    consultar=str(input('Quer os dados de qual jogador? \n')).strip().title()
    if consultar == '':
        break
    if consultar in time:
        print(f'\nDados de {consultar}:')
        for i, g in enumerate(time[consultar]['gols']):
            print(f'  Partida {i + 1}: {g} gol(s)')
    else:
        print('Jogador não encontrado.')