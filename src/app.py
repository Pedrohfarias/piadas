from flask import Flask

from formata_piadas import piadas_perguntas_respostas

app = Flask(__name__)

@app.route("/perguntas", methods=["GET"])
def piadas():
    return piadas_perguntas_respostas()

if __name__ == "__main__":
    app.run()
