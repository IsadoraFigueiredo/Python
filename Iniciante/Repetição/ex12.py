#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.

def sequencia(termo_anterior, termo_atual):
    while termo_atual <= 500:
        
        proximo_termo = termo_anterior + termo_atual
        if proximo_termo<=500:
            print(proximo_termo)

            termo_anterior = termo_atual
            termo_atual = proximo_termo

termo_anterior = 0
termo_atual = 1

print(termo_anterior)
print(termo_atual)
sequencia(termo_anterior, termo_atual)
