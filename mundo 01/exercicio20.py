from random import shuffle

a1 = input('Digite o nome do primero aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
shuffle(lista)


print('A ordem que os alunos se apresentarão será:')
print(lista)
