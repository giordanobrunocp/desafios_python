dados=[]
soma=0
mulheres=[]
maiores=[]

while True:
    nome=str(input('Nome: ')).strip().title()
    temp = {}
    if nome == '':
        break
    temp['nome'] = nome

    sexo=str(input('Sexo: [M/F]: ')).upper()[0]
    temp['sexo'] = sexo

    idade=int(input('Idade: '))
    temp['idade'] = idade
    dados.append(temp)

for pessoa in dados:
    soma+=pessoa['idade']
    media=(soma/len(dados))
for mulher in dados:
    if mulher['sexo'] == 'F':
        mulheres.append(mulher['nome'])
for maior in dados:
    if maior['idade']>media:
        maiores.append(maior['nome'])

print(dados)
print(f'Foram cadastradas {dados} pessoas')
print(f'A média de idade das pessoas cadastradas foi {media:.2f} anos')
print(f'As {len(mulheres)} mulheres cadastras foram: {mulheres}')
print(f'{len(maiores)} pessoas maiores que a média de idade: {maiores}')