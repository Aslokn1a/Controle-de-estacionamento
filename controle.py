import numpy as np
import random 

a = np.array(["0","0","0","0","0"])
b = np.array(["0","0","0","0","0"])
c = np.array(["0","0","0","0","0"])
#print(random.choice([a, b, c]))


#código para configuração do menu
def start():
    while True:
        print("\nMenu: ")
        print("1. Alocar vaga: ")
        print("2. Liberar vaga: ")
        print("3. exibir vagas: ")
        print("4. consultar veiculo")
        print("5. sair")
        choice = input("Informe a ação desejada: ")
        if choice == "1":
            print("placeholder do alocar(colocar a função aqui genio)")
        elif choice == "2":
            print("placeholder do liberar(colocar a função aqui genio)")
        elif choice == "3": 
            print("placeholder do exibir(colocar a função aqui genio)")
        elif choice == "4":
            print("placeholder do consultar(colocar a função aqui genio)")
        elif choice == "5":
            break
        else:
            print("Opção inválida, por favor informe um número entre 1 a 5 de acordo com as identificações feitas")

start()