# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

def classificar_turma(media_idades):
    if 0 <= media_idades <= 25:
        return "jovem"
    elif 26 <= media_idades <= 60:
        return "adulta"
    else:
        return "idosa"


idades = []
soma_idades = 0

n = int(input("Quantas pessoas há na turma? "))

for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)
    soma_idades += idade

media_idades = soma_idades / n

print("A média de idade da turma é:", media_idades)
print("A turma é classificada como:", classificar_turma(media_idades))

