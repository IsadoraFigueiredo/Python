#Defina o tipo do triângulo utilizando classe

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 != self.lado2 != self.lado3 != self.lado1:
            return "Escaleno"
        else:
            return "Isósceles"

# Exemplo de uso
triangulo = Triangulo(5, 5, 5)
print("O triângulo é:", triangulo.tipo_triangulo())
