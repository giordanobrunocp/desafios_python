primeirotermo=int(input('Primeiro termo: '))
razao=int(input('Razao: '))
c=int(input('Termos: '))

while c>0:
    print(primeirotermo, end=' ')
    c-=1
    primeirotermo=primeirotermo+razao
