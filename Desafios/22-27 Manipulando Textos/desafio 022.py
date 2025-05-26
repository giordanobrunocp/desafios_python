nome=input('Digite seu nome completo').strip().title()

print ('Seu nome em maiúsculo é {}'.format(nome.upper()))
print ('Seu nome em minúsculo é {}'.format(nome.lower()))
print ('Seu nome inteiro possuí {} letras' .format(len(nome.replace(' ',''))))
print ('Seu primeiro nome é {} e ele possui {} letras' .format(nome.split()[0],len(nome.split()[0])))