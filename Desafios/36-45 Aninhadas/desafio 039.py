from datetime import  date
ano=date.today().year
nascimento=int(input('Digite seu ano de nascimento: '))
idade=ano-nascimento

if idade < 18:
    print('Ainda não é hora de se alistar, faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade > 18:
    print('Você já passou da data para se alistar à {} anos.'.format(idade-18))