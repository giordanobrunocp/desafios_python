casa=float(input('Qual o valor da casa ? '))
salario=float(input('Qual o valor do seu salário? '))
anos=int(input('Em quantos anos você deseja financiar? '))
meses=anos*12
parcela=casa/meses
 
if (parcela <= (0.3*salario)):
    print('FINANCIAMENTE APROVADO! \n Sua parcela será de R${:.2f}, em {} vezes'.format(parcela,meses))
else:
    print('Sentimos muito, o financiamento não foi aprovado...')