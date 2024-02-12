#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

def calcular_H(N):
    H = 0
    for i in range(1, N + 1):
        H += 1 / i
    return H

N = int(input("Digite o valor de N: "))
valor_H = calcular_H(N)
print(f"O valor de H com {N} termos é: {valor_H:.6f}")
