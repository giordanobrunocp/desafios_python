import random
a1=input('Digite o nome do aluno 1 ')
a2=input('Digite o nome do aluno 2 ')
a3=input('Digite o nome do aluno 3 ')
a4=input('Digite o nome do aluno 4 ')

input('Pressione enter para iniciar')
aluno=random.choice([a1,a2,a3,a4])

print('Dentre os alunos {}, {}, {} e {}. O escolhido foi o {}'.format(a1,a2,a3,a4,aluno))
