#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


def ler_numeros():
    numeros = []
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)
    return numeros

def calcular_soma(numeros):
    return sum(numeros)

def calcular_multiplicacao(numeros):
    multiplicacao = 1
    for num in numeros:
        multiplicacao *= num
    return multiplicacao


numeros = ler_numeros()
soma = calcular_soma(numeros)
multiplicacao = calcular_multiplicacao(numeros)


print("Soma:", soma)
print("Multiplicação:", multiplicacao)
print("Números digitados:", numeros)

