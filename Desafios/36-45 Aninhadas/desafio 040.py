n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
n3=float(input('Digite sua terceira nota: '))

media=(n1+n2+n3)/3
print('Sua média é {:.2f}'.format(media))
if media <5:
    print('Você está REPROVADO...'.format(media))
elif 6.9 >= media:
    print('Você precisa de uma recuperação.')
elif media >= 7:
    print('Você está APROVADO!!!')