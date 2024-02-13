#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.


def ler_numeros():
    vetor = []
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número real: "))
        vetor.append(numero)
    return vetor


def ordem_inversa(vetor):
    print("Números na ordem inversa:")
    for numero in reversed(vetor):
        print(numero)


vetor = ler_numeros()
ordem_inversa(vetor)
