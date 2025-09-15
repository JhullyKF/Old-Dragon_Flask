from flask import Flask, redirect, request, url_for, render_template
from models.personagem import Personagem

from models.raca.humano import Humano
from models.raca.elfo import Elfo
from models.raca.halfling import Halfling
from models.raca.anao import Anao
from models.classe.guerreiro import Guerreiro
from models.classe.clerigo import Clerigo
from models.classe.ladrao import Ladrao
from uteis.dado import Dado
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/criar-personagem", methods=["POST"])
def criar_personagem():
    if request.method == "POST":
        nome = request.form["nome"]
        raca_value = int(request.form["raca"])
        classe_value = int(request.form["classe"])
        aventura_value = int(request.form["aventura"])

        raca = define_raca(raca_value)
        classe = define_classe(classe_value)
        
        personagem = Personagem(nome, raca, classe)

        match aventura_value:
            case 1: aventura_classica(personagem)
            case 2: aventura_aventureira(personagem)

        image_file = define_imagem(personagem)
        return render_template("ficha.html", personagem=personagem, criado=True, image_file=image_file)

def define_raca(raca_value):
    match raca_value:
        case 1: 
            return Anao()
        case 2: 
            return Elfo()
        case 3: 
            return Humano()
        case _:
            return Halfling()
        
def define_classe(classe_id):
    match classe_id:
        case 1: 
            return Ladrao()
        case 2:
            return Guerreiro()
        case _:
            return Clerigo()

def define_imagem(personagem):
    images={
            "Mago": "images/mago.png",
            "Ladrão": "images/ladrao.png",
            "Guerreiro": "images/guerreiro.png",
            "Clérigo": "images/clerigo.png"
        }
    return images.get(personagem.classe.titulo)

def aventura_classica(personagem):
    resultados = [Dado.rodar_3d6() for _ in range(6)]

    for i, a in enumerate(personagem.atributos):
        personagem.atributos[a] = resultados[i]

def aventura_aventureira(personagem):
    resultados = [Dado.rodar_3d6() for _ in range(6)]
    redirect(url_for("atribuir.html"), resultados)



if __name__ == "__main__":
    app.run(debug=False)