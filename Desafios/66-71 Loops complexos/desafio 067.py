while True:
    print(20*'=')
    num = int(input('Digite um valor (digite um valor negativo para encerrar): '))
    if num<0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
print('Encerrando...')
