cid=input('Digite o nome da sua cidade: ').strip().upper()

#print (cid.upper().split()[0].find('SANTO'))

print ('Sua cidade começa com Santo? {}' .format(cid[0:5] == 'SANTO'))