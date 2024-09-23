import numpy as np
import random 

a = np.array([])
b = np.array([])
c = np.array([])

#a = np.full(5, None)  # Setor A com 5 vagas
#b = np.full(5, None)  # Setor A com 5 vagas
#c = np.full(5, None)  # Setor A com 5 vagas
#print(random.choice([a, b, c]))

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj][0][0]
    
def ocupar(a,b,c,car):
    
    x = np.random.randint(3)
    match x:
        case 0:
            if a.size == 0:
                a = np.append(a,car)
                return()
            elif not np.isin(car, a):
                a = np.append(a,car)
                return()
            else:
                return(print("Placa já Registrada"))
        case 1:
            if b.size == 0:
                b = np.append(b,car)
                return()
            elif not np.isin(car, b):
                b = np.append(b,car)
                return()
            else:
                return(print("Placa já Registrada"))
        case 2:
            if c.size == 0:
                c = np.append(c,car)
                return()
            elif not np.isin(car, c):
                c = np.append(c,car)
                return()
            else:
                return(print("Placa já Registrada"))



def consultar(a,b,c,car):
    for setor in [a, b, c]:
        if car in setor:
            vaga_oc = np.where(setor == car)[0][0]
            print(f"\nO carro {car} está na vaga {vaga_oc+1} do setor {namestr(setor,globals())}")
            return
    print(f"\nVeículo {car} não está estacionado.")
def liberar(a,b,c,car):
    for setor in [a, b, c]:
        if car in setor:
            vaga_oc = np.where(setor == car)[0][0]
            setor[vaga_oc] = None
            print(f"\nVeículo {car} removido da vaga {vaga_oc+1}.")
            return True
    
    print("\nVeículo não encontrado.")
    return False


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
            car = str(input("informe a placa do veículo: "))
            ocupar(a,b,c,car)
        elif choice == "2":
            car = str(input("informe a placa do veículo: "))
            liberar(a,b,c,car)
        elif choice == "3": 
            print("placeholder do exibir(colocar a função aqui genio)")
        elif choice == "4":
            car = str(input("informe a placa do carro desejado: "))
            consultar(a,b,c,car)
        elif choice == "5":
            break
        else:
            print("Opção inválida, por favor informe um número entre 1 a 5 de acordo com as identificações feitas")

start()