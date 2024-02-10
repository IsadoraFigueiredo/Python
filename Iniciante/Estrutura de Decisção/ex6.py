print("Responda 'sim' ou 'não' para as perguntas a seguir:")

# Inicializa o contador de respostas positivas
resposta = 0

# Faz as 5 perguntas
telefonou = input("Telefonou para a vítima? ")
if telefonou == 'sim':
    resposta += 1

local_crime = input("Esteve no local do crime? ")
if local_crime == 'sim':
    resposta += 1

mora_perto = input("Mora perto da vítima? ")
if mora_perto == 'sim':
    resposta += 1

devia_vitima = input("Devia para a vítima? ")
if devia_vitima == 'sim':
    resposta += 1

trabalhou_vitima = input("Já trabalhou com a vítima? ")
if trabalhou_vitima == 'sim':
    resposta += 1

# Classifica a pessoa com base no número de respostas positivas
if resposta == 2:
    print("Você é suspeito(a)!")
elif 3 <= resposta <= 4:
    print("Você é cúmplice!")
elif resposta == 5:
    print("Você é o(a) assassino(a)!")
else:
    print("Você é inocente!")
