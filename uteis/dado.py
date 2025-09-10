import random
from abc import ABC

class Dado(ABC):
    def rodar_3d6():
        resultado = 0
        for i in range(3):
            resultado += random.randrange(1, 7)
        return resultado
    
    def rodar_4d6():
        resultado = []
        for i in range(4):
            resultado.append(random.randrange(1, 7))
        return resultado
