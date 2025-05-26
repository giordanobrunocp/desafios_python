tupla=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número inteiro de 0 a 20: ').strip())
    if 0 < num < 20:
        print(f'O número {num} em extenso fica {tupla[num]}')
        continue
    print('Número invalido, tente novamente.')

