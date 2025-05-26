num=int(input('Digite quantos termos de fibonacci gostaria de saber: '))#0,1,1,2,3,5,8,13,21,34,55
lista=[0,1]
for c in range(0,num-2):
    fibo=lista[0+c]+lista[1+c]
    lista.append(fibo)
print(lista, end=' ')

