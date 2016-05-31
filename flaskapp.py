from flask import Flask, jsonify, request, send_from_directory
from json import dumps

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

registroAlunni = {"0":{"numeroReg":"0","nome":"indefinito","cognome":"indefinito","annoNascita":"1900"}}

@app.route("/")
def index():
   return send_from_directory('static/', 'index.html')

@app.route("/js/<nomeFile>")
def caricaJS(nomeFile):
   return send_from_directory('static/js/', nomeFile)
   return ""

@app.route("/alunnoByNumeroReg/", methods=["POST"])
def alunnoByNumeroReg():
   numeroReg = request.json['numeroReg']
   dizAlunno = registroAlunni[numeroReg]
   stringJson = jsonify ( ** dizAlunno )
   return stringJson

@app.route("/inserisciAlunnoPOST/", methods=["POST"])
def inserisciAlunnoPOST():
   numeroReg =    request.json['numeroReg']
   nome =         request.json['nome']
   cognome =      request.json['cognome']
   annoNascita =  request.json['annoNascita']
   dizAlunno = {"numeroReg": numeroReg, "nome":nome, "cognome":cognome, "annoNascita":annoNascita}
   registroAlunni[numeroReg] = dizAlunno
   return dumps({"success": True})

if __name__=="__main__":
   app.run()


