from abc import ABC, abstractmethod
class Raca(ABC):
    def __init__(self, titulo, descricao, movimento, infravisao, alinhamento, habilidades):
        self.titulo = titulo
        self.descricao = descricao
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

    @abstractmethod
    def exibir_dados(self):
        pass
    
    @abstractmethod
    def exibir_habilidades(self):
        pass
    
    def __str__(self):
        return f"{self.titulo}"