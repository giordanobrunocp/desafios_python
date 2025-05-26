from datetime import date
dados={}

nome=str(input('Nome: '))
dados['nome']=nome

ano=int(input('Ano de nascimento: '))
idade=date.today().year - ano
dados['Idade']=idade

carteira=int(input('Carteira de trabalho: '))
dados['Carteira']=carteira

if carteira!=0:
    contrato=int(input('Ano do primeiro contrato: '))
    dados['Contrato']=contrato

    salario=float((input('Salário: ')))
    dados['Salario']=salario

    contribuidos=(35-(date.today().year - contrato))
    dados['Anos para aposentar']=contribuidos


for k, v in dados.items():
    print(f'{k} tem o valor {v}')
