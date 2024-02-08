#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

while True:
    altura_str = input("Digite sua altura em metros: ")
    if "," in altura_str:
        print("Por favor, digite a altura usando ponto (.) ao invés de vírgula (,).")
    else:
        altura = float(altura_str)
        peso_ideal = calcular_peso_ideal(altura)
        print("Seu peso ideal é:", peso_ideal, "quilogramas")
        break
       
