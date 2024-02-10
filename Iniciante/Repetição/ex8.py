#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.



user = input("Insira o nome do usuario: ")
password = input ("Insira a senha: ")
while password == user:
    print("Senha invalida! \nA senha deve ser diferente do usuario!")
    password = input ("Insira a senha: ")
