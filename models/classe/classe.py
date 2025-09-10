from abc import ABC, abstractmethod

class Classe(ABC):
    def __init__(self, titulo, ataque, vida, armas, armaduras, itens, habilidades):
        self.titulo = titulo
        self.ataque = ataque
        self.vida = vida
        self.armas = armas
        self.armaduras = armaduras
        self.itens = itens
        self.habilidades = habilidades
    
    @abstractmethod
    def exibir_dados(self):
        pass
    
    def __str__(self):
        return f"{self.titulo}"