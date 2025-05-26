preco=float(input('Qual é o valor do produto? R$'))
pagamento=int(input('Qual será a forma de pagamanto?\n Digite 1 para Dinheiro ou Pix \n Digite 2 para Cartão de crédito\n'))
if pagamento==1:
    print('O valor do produto no PIX/Dinheiro será de R${}'.format(preco*0.90))
elif pagamento==2:
    parcela=int(input('Em quantas parcelas?\n'))
    if parcela<=2:
        print('O valor ficará em {} parcelas de R${}'.format(parcela, preco/parcela))
    elif parcela>2:
        print('O valor ficará em {} parcelas de R${}'.format(parcela, (preco*1.20)/parcela))
