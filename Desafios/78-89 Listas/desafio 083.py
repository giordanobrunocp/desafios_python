exp=input('Digite uma expressão matemática: ')
esquerda=(exp.count('('))
direita=(exp.count(')'))

if esquerda==direita:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')
