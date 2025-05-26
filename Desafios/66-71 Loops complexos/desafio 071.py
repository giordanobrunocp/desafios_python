saque=int(input('Quanto deseja sacar? R$'))
n50=0
n20=0
n10=0
n01=0

while saque >= 50:
    saque-=50
    n50+=1
    if saque <50:
        while saque >= 20:
            saque-=20
            n20+=1
            if saque < 20:
                while saque >= 10:
                    saque-=10
                    n10+=1
                    if saque < 10:
                        while saque >=1:
                            saque-=1
                            n01+=1

print(f'Total de {n50} notas de R$ 50,00')
print(f'Total de {n20} notas de R$ 20,00')
print(f'Total de {n10} notas de R$ 10,00')
print(f'Total de {n01} notas de R$ 1,00')
