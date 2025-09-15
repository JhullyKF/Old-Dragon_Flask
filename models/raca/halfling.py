from models.raca.raca import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__("Halfling", "Os mais Perspicazes e Curiosos Aventureiros.", 6, 0, 
                         "neutro", habilidades=["Furtivo", "Destemido", "Bons de Mira", 
                                               "Pequenos", "Restrições"])

    def __str__(self):
        return super().__str__()