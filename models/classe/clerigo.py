from models.classe.classe import Classe

class Clerigo(Classe):
    def __init__(self):
        super().__init__("Clérigo", 1, 8, armas = ["Armas impactantes"], armaduras = ["Todas"], 
                         itens=["Ordeiros"], 
                         habilidades={"Magias Divinas" : 1, "Afastar Mortos-Vivos" : 1, 
                                      "Cura Milagrosa" : 1})
        
    def __str__(self):
        return super().__str__()