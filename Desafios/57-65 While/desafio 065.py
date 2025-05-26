lista=[]
num=0
continuar='S'

while continuar=='S':
    num=int(input('Digite um número: '))
    lista.append(num)
    continuar= input('Deseja continuar? [S/N]').strip().upper()[0]

print('A média dos números digitados foi {:.2f}, o maior número foi {} e o menor número foi {}'.format(sum(lista)/len(lista),max(lista),min(lista)))