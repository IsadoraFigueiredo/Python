#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um 
#grande quantidade de organizações O programa deverá ler os valores até ser informado o valor 0, 
#que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa 
#(0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados 
#terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e 
#informar o vencedor da enquete.

def calcular_porcentagem(votos, total_votos):
    return [(voto / total_votos) * 100 for voto in votos]

def enquete_sistemas():
    votos = [0, 0, 0, 0, 0, 0]  # Lista para armazenar os votos para cada sistema operacional
    while True:
        print("\nQual o melhor Sistema Operacional para uso em servidores?")
        print("1- Windows Server")
        print("2- Unix")
        print("3- Linux")
        print("4- Netware")
        print("5- Mac OS")
        print("6- Outro")
        print("0- Sair")
        
        opcao = int(input("Digite o número correspondente à sua escolha: "))
        
        if opcao == 0:
            break
        elif 1 <= opcao <= 6:
            votos[opcao - 1] += 1  # Incrementa o voto para o sistema escolhido
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    total_votos = sum(votos)
    porcentagens = calcular_porcentagem(votos, total_votos)
    opcao_mais_votada = votos.index(max(votos)) + 1

    print("\nResultado da enquete:")
    print("O total de votos")
    print("Windows Server:", votos[0], "votos -", f"{porcentagens[0]:.2f}%")
    print("Unix:", votos[1], "votos -", f"{porcentagens[1]:.2f}%")
    print("Linux:", votos[2], "votos -", f"{porcentagens[2]:.2f}%")
    print("Netware:", votos[3], "votos -", f"{porcentagens[3]:.2f}%")
    print("Mac OS:", votos[4], "votos -", f"{porcentagens[4]:.2f}%")
    print("Outro:", votos[5], "votos -", f"{porcentagens[5]:.2f}%")
    print("\nA opção mais votada foi a", opcao_mais_votada)

# Executa a função da enquete
enquete_sistemas()
