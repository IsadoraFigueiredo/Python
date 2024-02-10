#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de
# um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 # Média de Aproveitamento  Conceito
 # Entre 9.0 e 10.0        A
 # Entre 7.5 e 9.0         B
 # Entre 6.0 e 7.5         C
 # Entre 4.0 e 6.0         D
 # Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
#e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def calcular_media(nota1, nota2):
    
    media = (nota1 + nota2)/2
    return media

def conceito(media):
    if 9<=media<=10:
        return "Aprovado, conceito A" 
    elif 7.5 <= media < 9:
        return "Aprovado, conceito B"
    elif 6 <= media < 7.5:
        return "Aprovado, conceito C"
    else:
        return "Reprovado"

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = calcular_media(nota1,nota2)

resultado = conceito(media)
print("O aluno está:", resultado)

