from models.classe.classe import Classe

class Ladrao(Classe):
    def __init__(self):
        super().__init__("Ladrão", 1, 6, armas = ["Pequenas", "Médias"], armaduras = ["Leves"], 
                         itens=["Pergaminho de protecao"], 
                         habilidades={"Ataque furtivo": 1, "Ouvir ruidos": 1, "Talentos de ladrao": 1})
        
    def __str__(self):
        return super().__str__()