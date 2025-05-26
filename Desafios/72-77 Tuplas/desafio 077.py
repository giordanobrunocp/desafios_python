tupla=('abacaxi', 'elefante', 'computador', 'universo', 'orquestra',
    'imagem', 'batata', 'estrela', 'mouse', 'cadeira',
    'paralelepipedo', 'aquarela', 'ventilador', 'hipopotamo',
    'azulejo', 'girassol', 'banana', 'formigueiro', 'oceano', 'edredom'
)

for n in range(0,len(tupla)):
    print('A palavra:', tupla[n])
    letras=((tupla[n])[0:])
    if letras.count('a') != 0:
        print(' Letras A=',letras.count('a'))
    if letras.count('e') != 0:
        print(' Letras E=',letras.count('e'))
    if letras.count('i') != 0:
        print(' Letras I=',letras.count('i'))
    if letras.count('o') != 0:
        print(' Letras O=',letras.count('o'))
    if letras.count('u') != 0:
        print(' Letras U=',letras.count('u'))
    print('\n')
