from flask import Flask, redirect, request, session, url_for, render_template
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
app.secret_key = 'minha_chave_secreta_aqui' 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/criar-personagem", methods=["POST"])
def criar_personagem():
    if request.method == "POST":
        session['nome'] = request.form["nome"].capitalize()
        session['raca_value'] = int(request.form["raca"])
        session['classe_value'] = int(request.form["classe"])
        aventura_value = int(request.form["aventura"])
        

        if aventura_value == 1:
            personagem = Personagem(session.get('nome'), define_raca(session.get('raca_value')), define_classe(session.get('classe_value')))
            image_file = define_imagem(personagem.classe)
            resultados = [Dado.rodar_3d6() for _ in range(6)]
            for i, a in enumerate(personagem.atributos):
                personagem.atributos[a] = resultados[i]
            return render_template("ficha.html", personagem=personagem, criado=True, image_file=image_file)
        
        elif aventura_value == 2:
            resultados = sorted([Dado.rodar_3d6() for _ in range(6)], reverse=True) 
            print(resultados)
            return salva_dados_aventura(resultados)
        
        elif aventura_value == 3:
            resultados = []
            valores = sorted([Dado.rodar_4d6() for _ in range(6)])
            print("valores: ", valores)
            for v in sorted(valores):
                resultado = sum(sorted(v)[1:])
                resultados.append(resultado)
            print(resultados)
            return salva_dados_aventura(resultados)  

def salva_dados_aventura(resultados):
            session['resultados'] = resultados
            resultados_com_id = list(enumerate(resultados)) 
            session['atributos_key'] =["Forca", "Destreza", "Constituicao", "Inteligencia", "Sabedoria", "Carisma"]
            return render_template("atribuir.html", atributos_key=session.get('atributos_key'), resultados=resultados_com_id)


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

def define_imagem(classe):
    images={
            "Mago": "images/mago.png",
            "Ladrão": "images/ladrao.png",
            "Guerreiro": "images/guerreiro.png",
            "Clérigo": "images/clerigo.png"
        }
    return images.get(classe.titulo)

@app.route("/definir-atributos", methods=["POST", "GET"])
def atribuir_atributos():
    personagem = Personagem(session.get('nome'), define_raca(session.get('raca_value')), define_classe(session.get('classe_value')))
    resultados = session.get('resultados')

    for atributo in session.get('atributos_key'):
        chave_do_form = atributo.lower()
        id_selecionado_str = request.form.get(chave_do_form)
        
        if id_selecionado_str:
            id_selecionado = int(id_selecionado_str)
            valor_final = resultados[id_selecionado]
            personagem.atributos[atributo] = valor_final
    image_file = define_imagem(personagem.classe)
    return render_template("ficha.html", personagem=personagem, criado=True, image_file=image_file)


if __name__ == "__main__":
    app.run(debug=False)