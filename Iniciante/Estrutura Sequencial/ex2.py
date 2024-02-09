#Confirme se 3 segmentos de retas são um triângulo, caso seja
#Retorne o tipo de triângulo: escaleno, isosceles e equilatero

def triangulo(a,b,c):

    if a+b>c and b+c>a and a+c>b:
        print ("É um triangulo")
        if a==b==c:
            return "EQUILATERO!"
        elif a==b or b==c or a==c:
            return "ISOSCELES"
        else:
            return "ESCALENO!"
    else:
        return "Não é um triangulo"

a=float(input("Informe o tamnho do primeiro segmento de reta: "))
b=float (input("Informe o tamnho do segundo segmento de reta: "))
c=float(input("Informe o tamnho do terceiro segmento de reta: "))

resultado = triangulo(a, b, c)
print(resultado)
