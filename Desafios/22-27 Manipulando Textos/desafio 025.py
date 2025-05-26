#nome=input('Digite seu nome completo: ')

#print(nome.upper().count('SILVA'))

nome=input('Digite seu nome: ').strip().upper()
print ('Seu nome tem Silva? {}'.format('SILVA' in nome))