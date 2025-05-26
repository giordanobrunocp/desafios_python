dias=int(input('Quantos dias alugado?'))
km = float(input('Quantos km rodados?'))

vdias=dias*60
vkm=km*0.15
total=vdias+vkm

print('O total a ser pago é de R${:.2f}'.format(total))
