classificacao=('Palmeiras', 'Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Ceará', 'Bahia', 'Fluminense', 'Corinthians',
               'Atlético-MG', 'Botafogo', 'São Paulo', 'Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional',
               'Vitória', 'Grêmio', 'Juventude', 'Santos', 'Sport')

print(f'Os cinco primeiros classificados são: {classificacao[:5]}' )
print(f'Os ultimos quatro na classificação são {classificacao[-4:]}')
print(f'Em ordem alfabética: {sorted(classificacao)}')
print(f'O Santos está na classificação {classificacao.index("Santos")+1}')