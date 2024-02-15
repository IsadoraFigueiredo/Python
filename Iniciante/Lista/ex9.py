#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
#Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
#considerando um que a gasolina custe R$ 2,25 o litro.  Os dados podem mudar a cada execução do programa.

def ler_dados_carros():
    modelos = []
    consumos = []
    for i in range(5):
        modelo = input(f"Digite o modelo do {i+1}º carro: ")
        consumo = float(input(f"Digite o consumo em km/l do {i+1}º carro: "))
        modelos.append(modelo)
        consumos.append(consumo)
    return modelos, consumos

def encontrar_modelo_mais_economico(modelos, consumos):
    indice_mais_economico = consumos.index(min(consumos))
    modelo_mais_economico = modelos[indice_mais_economico]
    return modelo_mais_economico

def calcular_consumo_e_custo(modelos, consumos, distancia, preco_gasolina):
    print("\nRelatório de Consumo")
    print("-" * 25)
    modelo_mais_economico = encontrar_modelo_mais_economico(modelos, consumos)
    print(f"Modelo mais econômico: {modelo_mais_economico}")
    print("\nConsumo para percorrer 1000 km:")
    for modelo, consumo in zip(modelos, consumos):
        litros_necessarios = distancia / consumo
        custo_total = litros_necessarios * preco_gasolina
        print(f"{modelo}: {litros_necessarios:.2f} litros - R$ {custo_total:.2f}")


distancia = 1000  # km
preco_gasolina = 2.25  # R$/litros


modelos, consumos = ler_dados_carros()
calcular_consumo_e_custo(modelos, consumos, distancia, preco_gasolina)
