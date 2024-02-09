#Faça um código que receba 3 números e retorne em ordem crescente

def crescente(num1, num2, num3):
    
    #coloca os numeros em uma lista
    numeros = [num1,num2,num3]
    #ordena
    numeros.sort()
    print("A ordem crescente: ", numeros)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

crescente(num1,num2,num3)