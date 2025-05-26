import random
a1=input('Informe o primeiro aluno: ')
a2=input('Informe o segundo aluno: ')
a3=input('Informe o terceiro aluno: ')
a4=input('Informe o quarto aluno: ')

alunos=([a1,a2,a3,a4])

input('Pressione <enter> para continuar')
escolhidos=random.sample(alunos,4)
print(escolhidos)
