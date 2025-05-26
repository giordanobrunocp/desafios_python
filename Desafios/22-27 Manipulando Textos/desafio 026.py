frase=input('Digite uma frase: ').strip().lower()

print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A letra "a" aparece primeiro na posição', frase.find('a'))
print('A letra "a" aparece por ultimo na posição',frase.rfind('a'))