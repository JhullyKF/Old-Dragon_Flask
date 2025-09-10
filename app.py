from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
#pagina com o fomulário
def index():
    if request.method == "POST":
        name = request.form["name"]
        race = request.form["race"]
        classe = request.form["classe"]
        return redirect(url_for("ficha", name=name, race=race, classe=classe))
    
    return render_template("index.html")

#formulário
@app.route("/ficha", methods=["GET", "POST"])
def ficha():
    name = request.form.get("name")
    race = request.form.get("race")
    classe = request.form.get("classe")
    images={
        "Mago": "images/mago.png",
        "Ladrão": "images/ladrao.png",
        "Guerreiro": "images/guerreiro.png",
        "Clérigo": "images/clerigo.png"
    }
    image_file = images.get(classe)

    return render_template("page.html", name=name, race=race, classe=classe, image_file=image_file)

if __name__ == "__main__":
    app.run(debug=True)