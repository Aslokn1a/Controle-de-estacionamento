import numpy as np

A = np.array(["1144AJC"])
B = np.array(["1144AJC"])
C = np.array(["1144AJC"])

def ocupar_vaga():
    global A,B,C
    placa = input("Escreva a Placa do Veículo: ")
    x = np.random.randint(3)
    match x:
        case 0:
            if A.size == 0:
                A = np.append(A,placa)
                return()
            elif not np.isin(placa, A):
                A = np.append(A,placa)
                return()
            else:
                return(print("Placa já Registrada"))
        case 1:
            if B.size == 0:
                B = np.append(B,placa)
                return()
            elif not np.isin(placa, B):
                B = np.append(B,placa)
                return()
            else:
                return(print("Placa já Registrada"))
        case 2:
            if C.size == 0:
                C = np.append(C,placa)
                return()
            elif not np.isin(placa, C):
                C = np.append(C,placa)
                return()
            else:
                return(print("Placa já Registrada"))

ocupar_vaga()
