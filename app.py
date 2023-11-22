from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def principal():
#     return "Bienvenid@ a mi sitio web con python - By Abdel de la cruz"

# @app.route('/contacto')
# def contacto():
#     return "Esta es la pagina de contactos"

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template("contactos.html")

@app.route('/lenguajes')
def mostrarLenguajes():
    lenguajes = ("PHP", "JAVA", "PYTHON", "C#", "JavaScript", "Perl", "Ruby")
    return render_template("lenguajes.html", lenguajes=lenguajes)

if __name__ == '_main_':
    app.run(debug=True)