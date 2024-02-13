#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

def ler_numeros():
    numeros = []
    for i in range(20):
        numero = int(input(f"Digite o {i+1}º inteiro: "))
        numeros.append(numero)
    return numeros

def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

print("Digite 20 numeros")
numeros=ler_numeros()
pares, impares = separar_pares_impares(numeros)
    
print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)

