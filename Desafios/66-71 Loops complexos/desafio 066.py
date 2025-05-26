soma=num=cont=0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos números digitados foi {soma} e foram somados {cont} números')