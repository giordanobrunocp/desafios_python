sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()[0]
'''c=0

while c==0:
    if sexo in ('M','F'):
        sexo = input('Digite o seu sexo (M/F): ').strip().upper()
    else:
        sexo = input('Erro! digite M para Masculino e F para Feminino (M/F): ').strip().upper()'''

while sexo not in ('M','F'):
    sexo = input('Erro! digite M para Masculino e F para Feminino (M/F): ').strip().upper()

if sexo == 'M':
    print('O sexo digitado foi M portanto Masculino.')
else:
    print('O sexo digitado foi F portanto Feminino.')
