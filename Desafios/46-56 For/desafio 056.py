h=[] #lista os homens
hi=[] #lista com as idades dos homens
m=[] #lista as mulheres
mi=[] #lista com as idades das mulheres
mmdi=0 #numero de mulheres maiores de idade
for c in range(1,5):
    nome=str(input('Digite um nome: '))
    idade=int(input('Digite a idade: '))
    sexo=str(input('Digite o sexo: [H/M]: ')).lower()
    if sexo=='h':
        h.append(nome)
        hi.append(idade)
    elif sexo=='m':
        m.append(nome)
        mi.append(idade)
    else:
        print('Erro 1, tente novamente.')

i=(hi.index(max(hi)))
velho=h[i]

print('O homem mais velho é o {} e ele possui {} anos' .format(velho,max(hi)))
print('A média de idade dos homens é {:.2f}'.format(sum(hi)/len(hi)))
print('A média de idade das mulheres é {:.2f}'.format(sum(mi)/len(mi)))
for c2 in range (0,len(mi)):
    if mi[c2]>18:
        mmdi+=1
print('Existem {} mulheres com mais de 18 anos.'.format(mmdi))
