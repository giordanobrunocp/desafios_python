num=int(input('Digite um número inteiro positivo:  '))
opcao=int(input('Para qual formato você deseja converter seu número?\n Digite 1 para binário\n Digite 2 para octal \n Digite 3 para hexadecimal \n'))
if opcao == 1:
      print('O número {} em binário é {}'.format(num,bin(num)))
elif opcao == 2:
    num=oct(num)
    print('O número {} em octal é {}'.format(num,oct(num)))
elif opcao == 3:
    num=hex(num)
    print('O número {} em hex é {}'.format(num,hex(num)))
