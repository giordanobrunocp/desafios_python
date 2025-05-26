salario=float(input('Digite seu salário atual R$'))
aumento=int(input('Digite o aumento desejado em %: '))
nsalario=salario*(1+(aumento/100))

print('Seu salário de R${:.2f}, com um aumento de {}% passará a ser de R${:.2f}'.format(salario,aumento,nsalario))