situ={}
alunos=[]

while True:
    nome=input('[Digite 999 para fechar] \nNome: ').strip().title()
    if nome == '999':
        break
    situ['nome']=nome
    media=float(input('Média: '))
    if media >= 6:
        situ['media']=media
        situ['situacao']='Aprovado'
    else:
        situ['media']=media
        situ['situacao']='Reprovado'
    alunos.append(situ.copy())

for c,a in enumerate(alunos):
    print(f'O aluno {alunos[c]['nome']}, com média {alunos[c]['media']} está {alunos[c]['situacao']}')