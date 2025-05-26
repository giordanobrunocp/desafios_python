tupla=('Notebook', '3500.00', 'Smartphone', '2100.00', 'Fone de Ouvido', '250.00', 'Cafeteira', '320.00', 'Teclado Mecânico', '480.00',
       'Smart TV', '2899.00', 'Cadeira Gamer', '1290.00', 'Headset', '399.00', 'Geladeira', '4590.00', 'Micro-ondas', '650.00')

print('-'*60)
print(f'{"LOJAS GIOBRAZ":^60}')
print('-'*60)

for n in range(0, len(tupla),2):
    print(f'{(tupla[n]):.<50}R${(tupla[n+1]): >8}')
