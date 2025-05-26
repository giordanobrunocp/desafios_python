soma=0
frase=str(input('Digite uma frase:  ')).strip().upper().replace(' ','')


for c in range(0,len(frase),1):
    if frase[c]==frase[-1-c]:
        soma += 1
if soma==len(frase):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')