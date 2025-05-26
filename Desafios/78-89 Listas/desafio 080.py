'''for c in range(0,5):
    num=int(input('Digite um valor: '))
    if num>lista[0]:
        lista.insert(0,num)
    elif num>lista[1]:
        lista.insert(1, num)
    elif num>lista[2]:
      lista.insert(2, num)
    elif num>lista[3]:
       lista.insert(3, num)
    elif num>lista[4]:
      lista.insert(4, num)
print(lista)'''

lista=[]

for c in range(0,5):
    num=int(input('Digite um valor: '))
    pos=0
    while pos<len(lista) and num>lista[pos]:
        pos+=1
    lista.insert(pos,num)

print(lista)