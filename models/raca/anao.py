from models.raca import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__("Anão", "Orgulhosos Habitantes dos Salões sob a Montanha.", 6, 18, 
                         "ordem", habilidades=["Mineradores", "Vigoroso", "Armas grandes", 
                                               "Inimigos"])

    