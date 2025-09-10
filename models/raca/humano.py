from models.raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", "Os mais Comuns,Versáteise Adaptáveis Aventureiros.", 9, 0, 
                         "qualquer", habilidades=["Aprendizado", "Adaptabilidade"])

    def exibir_dados(self):
        str = f"""Raça: {self.titulo} 
        \nDescrição: {self.descricao} 
        \nMovimento: {self.movimento} 
        \nInfravisão: {self.infravisao}
        \nAlinhamento: {self.alinhamento}"""
        return str

    def exibir_habilidades(self):
        str = f"""\nHabilidades: {self.habilidades}"""
        return str