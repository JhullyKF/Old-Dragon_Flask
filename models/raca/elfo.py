from models.raca import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", "Misteriosos, Longevos e Graciosos habitantes das Florestas.", 9, 18, 
                         "neutro", habilidades=["Percepção Natural", "Graciosos", "Treinamento Racial", 
                                               "Imunidades"])
