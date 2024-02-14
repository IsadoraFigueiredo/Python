#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def calcular_media(notas_alunos):
    return sum(notas_alunos) / len(notas_alunos)

def contar_alunos_aprovados(notas_alunos):
    return len([nota for nota in notas_alunos if nota >= 7.0])

alunos_aprovados = 0
notas_alunos = []

for i in range(10):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas_alunos.append(nota)

media = calcular_media(notas_alunos)
alunos_aprovados = contar_alunos_aprovados(notas_alunos)

print("Médias dos alunos:", media)
print("Número de alunos com média maior ou igual a 7.0:", alunos_aprovados)


