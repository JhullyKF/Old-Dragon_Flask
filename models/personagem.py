class Personagem:
    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = {
            "Forca": 0,
            "Destreza": 0,
            "Constituicao": 0,
            "Inteligencia": 0,
            "Sabedoria": 0,
            "Carisma": 0
        }
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_raca(self, raca):
        self.raca = raca
    
    def set_classe(self, classe):
        self.classe = classe
