from models.raca.raca import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", "Misteriosos, Longevos e Graciosos habitantes das Florestas.", 9, 18, 
                         "neutro", habilidades=["Percepção Natural", "Graciosos", "Treinamento Racial", 
                                               "Imunidades"])

    def __str__(self):
        return super().__str__()