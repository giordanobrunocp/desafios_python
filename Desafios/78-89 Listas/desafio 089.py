notas=[[],[],[]]

while True:
    nome=(str(input('Digite o nome do aluno: '))).title().strip()
    notas[0].append(nome)

    nota1=(float(input('Digite a primeira nota: ')))
    notas[1].append(nota1)

    nota2=(float(input('Digite a segunda nota: ')))
    notas[1].append(nota2)

    media=((nota1+nota2)/2)
    notas[2].append(media)

    continuar=input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar=='N':
        break
print(33*'_')
print('Nº    Nome                Média')
for e, nom in enumerate (notas[0]):
    print(f'{e:.<2}{nom:.<12}{notas[2][e]:.>16.1f}')

while True:
    consultar=str(input('Mostrar nota de qual aluno? [Digite 999 para encerrar]\n')).strip().title()
    if consultar in notas[0]:
        pos=notas[0].index(consultar)
        print(f'As notas do aluno {consultar} são {notas[1][pos*2]} e {notas[1][pos*2+1]}')
    if consultar == '999':
        print('Encerrando...')
        break