#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de 
#litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 
#R$ 2,50 o preço do litro do álcool é R$ 1,90.
import sys

def funcao_gasolina(litros):
    preco_gasolina = litros * 2.5
    return preco_gasolina

def funcao_alcool(litros):
    preco_alcool = litros * 1.9
    return preco_alcool

def preco_combustivel(litros, combustivel):
    if combustivel == 'G' or combustivel=='g':
        if 0 <= litros <= 20:
            novo_preco = funcao_gasolina(litros) * 0.96
        else:
            novo_preco = funcao_gasolina(litros) * 0.94
    elif combustivel == 'A' or combustivel =='a':
        if 0 <= litros <= 20:
            novo_preco = funcao_alcool(litros)*0.97
        else:
            novo_preco = funcao_alcool(litros)*0.95

    else:
        print("Tipo de combustível inserido incorreto. Saindo do programa.")
        sys.exit()
        
    return novo_preco

combustivel = input("Deseja colocar gasolina (G) ou álcool (A): ")
litros = float(input("Quantos litros de combustível?: "))

novo_preco = preco_combustivel(litros, combustivel)

print("O total a pagar é: ", novo_preco)
