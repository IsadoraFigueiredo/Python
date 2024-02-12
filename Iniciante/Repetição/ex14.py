#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321

def inverter_numero(numero):
    numero_invertido = int(str(numero)[::-1])
    return numero_invertido

numero = int(input("Digite um numero inteiro positivo: "))

while numero <= 0:
    numero = int(input("Por favor, digite um numero inteiro positivo: "))

numero_invertido = inverter_numero(numero)
print("Número invertido:", numero_invertido)
