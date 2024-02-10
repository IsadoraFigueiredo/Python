#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 
#3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que 
#calcule e escreva o número de anos necessários para que a população  do país A ultrapasse ou iguale a 
#população do país B, mantidas as taxas de crescimento.

#Crescimento populção A: fa(x) = 80,000 x (1,03)^x   >>> x é igual ao ano
#Crescimento população B: fb(x) = 200,000 x (1,015)^x
#Queremos saber qual valor de x para que  fa>fb

def populacao_A(x):
    fa = 80000*((1.03)**x)
    return fa

def populacao_B(x):
    fb = 200000*((1.015)**x)
    return fb

x=1
fa = populacao_A(x)
fb = populacao_B(x)

while fb>=fa:
    x+= x
    fa = populacao_A(x)
    fb = populacao_B(x)
    
print("Após", x, "anos, a população A ultrapassa a população B.")