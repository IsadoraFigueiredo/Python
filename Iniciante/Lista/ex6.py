#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        elemento = int(input(f"Elemento {i + 1}: "))
        vetor.append(elemento)
    return vetor

def intercalar_vetores(vetor1, vetor2):
    vetor_intercalado = []
    for i in range(len(vetor1)):
        vetor_intercalado.append(vetor1[i])
        vetor_intercalado.append(vetor2[i])
        
    return vetor_intercalado

# Leitura dos vetores
print("Primeiro vetor:")
vetor1 = ler_vetor(10)

print("\nSegundo vetor:")
vetor2 = ler_vetor(10)

vetor3 = intercalar_vetores(vetor1, vetor2)


print("\nTerceiro vetor intercalado:", vetor3)
