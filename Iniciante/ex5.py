#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
#informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import sys

def calcular_delta(a,b,c):
    delta = (b)**2 - 4*a*c
    return delta

def calcular_raiz(delta):
    if delta>=0:
        raiz1 =  (-b - (delta)**(1/2)) /(2*a)
        raiz2 =  (-b + (delta)**(1/2)) /(2*a)
        return raiz1, raiz2
    else:
        return "Não há raiz"
    
a=float(input("Informe o valor da constante a: "))
if a=0:
    print("Não é uma equaçao do segundo grau!")
    sys.exit()
    
b=float(input("Informe o valor da constante b: "))
c=float(input("Informe o valor da constante c: "))

delta = calcular_delta(a,b,c)
raiz = calcular_raiz(delta)
print("As raízes são: ", raiz)
