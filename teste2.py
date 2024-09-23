import numpy as np
import random 

a = np.array(["1","0","0","0","0"])
#b = np.array(["2","0","0","0","0"])
#c = np.array(["3","0","0","0","0"])
#po=random.choice([a, b, c])
#d= np.where(a=="1")
#print(d)
#vaga_ocupada = np.where(setor == placa)[0][0]
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

my_numpy = np.zeros(2)
print(namestr(a, globals()))