from models.classe.classe import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__("Guerreiro", 1, 10, armas = ["Todas"], armaduras = ["Todas"], 
                         itens=["Pergaminho de protecao"], 
                         habilidades={"Maestria em arma" : 1, "Aparar" : 1, "Ataque extra" : 6})
        
    def __str__(self):
        return super().__str__()