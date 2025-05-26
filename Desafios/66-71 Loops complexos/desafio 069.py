continuar = 'S'
homens = 0  # homens cadastrados
todosmaior = 0  # pessoas maiores de idade
mulhermenor = 0  # mulheres com -20 anos

while continuar == 'S':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        continue

    idade = int(input('Digite a idade: '))

    if sexo == 'M':
        homens += 1
    if idade >= 18:
        todosmaior += 1
    if sexo == 'F' and idade <= 20:
        mulhermenor += 1

    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    while continuar not in ('N', 'S'):
        continuar = str(input('Opção inválida. Continuar? [S/N] ')).strip().upper()[0]

print('--' * 20)
print(f'Homens cadastrados: {homens}')
print(f'Mulheres menores de 20 anos cadastradas: {mulhermenor}')
print(f'Pessoas maiores de idade cadastradas: {todosmaior}')
