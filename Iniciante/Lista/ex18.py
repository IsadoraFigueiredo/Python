# Função para ler os caracteres e contar as consoantes

def contar_consoantes(vetor):
    consoantes = 0
    consoantes_lidas = []
    for caractere in vetor:
        if caractere.isalpha() and caractere not in "aeiouAEIOU":
            consoantes += 1
            consoantes_lidas.append(caractere)
    return consoantes, consoantes_lidas


vetor = []
print("Digite 10 caracteres:")
for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere: ").lower()
    vetor.append(caractere)
    
num_consoantes, consoantes = contar_consoantes(vetor)
print("\nForam lidas", num_consoantes, "consoantes.")
print("Consoantes lidas:", consoantes)


