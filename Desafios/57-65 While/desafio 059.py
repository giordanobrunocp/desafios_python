"""
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
comando=(input('''O que deseja fazer com estes números:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 9 ] Digitar novamente
[ 0 ] Sair
'''))

n1=n2=comando='9'

while comando in ('1','2','3','9'):
    if comando == '9':
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        comando = (input('''O que deseja fazer com estes números:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 9 ] Digitar novamente
[ 0 ] Sair
        '''))
    elif comando in ('1','2','3'):
        if comando == '1':
            print('A soma dos valores {} e {} é igual a {}'.format(n1,n2,n1+n2))
            comando = '9'
        elif comando == '2':
            print('A multiplicação dos números {} e {} é igual a {}' .format(n1,n2,n1*n2))
            comando='9'
        elif comando == '3':
           print('O maior número entre {} e {} é o {}'.format(n1,n2,max(n1,n2)))
           comando='9'

print('Saindo...')"""

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))

while True:
    print('=-='*30)
    comando=str(input('''Qual operação deseja realizar?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 9 ] Digitar novamente
    [ 0 ] Sair
    '''))
    if comando == '0':
        break
    elif comando == '1':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif comando == '2':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif comando == '3':
        print('O maior número entre {} e {} é {}'.format(n1,n2,max(n1,n2)))
    elif comando == '9':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('Comando errado!')

print('Saindo...')