from models.raca.raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", "O mais Comum,Versátil e Adaptável Aventureiro.", 9, 0, 
                         "qualquer", habilidades=["Aprendizado", "Adaptabilidade"])

    def __str__(self):
        return super().__str__()