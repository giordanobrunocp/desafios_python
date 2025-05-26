primeirotermo=int(input('Primeiro termo: '))
razao=int(input('Razao: '))
c=int(input('Termos: '))

while c > 0:
    while c>0:
        print(primeirotermo, end=' ')
        c=c-1
        primeirotermo=primeirotermo+razao

    c=int(input('Deseja mais quantos termos? '))

print ('Finalizando...')

