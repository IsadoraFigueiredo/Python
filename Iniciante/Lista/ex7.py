#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
#com mais de 13 anos possuem altura inferior à média de altura desses alunos.

def ler_idades_alturas():
    idades = []
    alturas = []
    for i in range(30):
        idade = int(input(f"Digite a idade do aluno {i+1}: "))
        altura = float(input(f"Digite a altura do aluno {i+1}: "))
        idades.append(idade)
        alturas.append(altura)
    return idades, alturas

def calcular_media(alturas):
    return sum(alturas) / len(alturas)

def alunos_inferior_media(idades, alturas):
    media_altura = calcular_media(alturas)
    alunos =0
    for i in range(len(idades)):
        if idades[i] > 13 and alturas[i] < media_altura:
            alunos += 1
    
    return alunos

idades, alturas = ler_idades_alturas()

print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {alunos_inferior_media(idades, alturas)}")



