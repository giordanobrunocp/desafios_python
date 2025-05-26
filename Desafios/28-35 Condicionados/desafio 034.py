salario=float(input('Qual o valor do seu salário atualmente? '))

if salario >1250.00:
    print('Seu novo salário será de R${:.2F}'.format(salario*1.1))
else:
    print('Seu salário será de R${:.2f}'.format(salario*1.15))