from flask import Flask, jsonify, render_template, request, send_from_directory
import sqlite3,os
        
        
        
app = Flask(__name__)

# se esiste var di env OPENSHIFT_DATA_DIR  siamo in opnshift
# se NON esiste siamo in localhost e DATA_DIR = '../data/'
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR','../data/')
pathDb  = os.path.join(DATA_DIR,'Alunni.db')

def initDB():
    ''' inizializza DB Sqlite'''
    # DB non esiste lo crea 
    conn = sqlite3.connect(pathDb)

    # crea le tabelle del DB se non esistono
    stringSQLTableAlunni = \
        "create table   if not exists  REGISTROALUNNI (\
            NUMEROREG integer primary key,\
            NOME      text not null,\
            COGNOME   text not null,\
            ANNONASCITA text not null\
        );"
        
    cursor = conn.cursor()
    cursor.execute(stringSQLTableAlunni)
    conn.commit()
    conn.close()

initDB()


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('indexTest.html')
    
@app.route("/alunnoByNumeroReg/", methods=["POST"]) # metodo POST
def alunnoByNumeroReg():
    # spedizione in formato html
    
    numeroReg = request.json['numeroReg']
    print numeroReg,"numREG"
    
    #apre connessione al DB per inserire un Alunno
    
    conn = sqlite3.connect(pathDb)
    print "Opened database successfully  ByNumero";
    cursor = conn.cursor()
    cur = cursor.execute("SELECT * FROM registroAlunni  WHERE NUMEROREG == ? ",[numeroReg]);
   
    #cursor = conn.execute("SELECT * FROM REGISTROALUNNI");
 
    
    # in questo caso e' atteso un solo elemento o nessuno: cursor e' una lista
    # di liste, ogni elemento e' una lista di valori corrispondenti alle chiavi
    # di un dizionario numeroReg | nome | cognome | annoNascita
    dizAlunno = {}
    for alunno in cur:
        numeroReg   =   alunno[0]
        nome        =   alunno[1]
        cognome     =   alunno[2]
        annoNascita =   alunno[3]
        
        dizAlunno = {"numeroReg": numeroReg, "nome": nome,
        "cognome": cognome, "annoNascita":annoNascita}
        
        break  #  al max un solo elemento viene letto
    print dizAlunno
    conn.commit()
    conn.close()
    # dizAluuno o e' diz vuoto oppure e' un solo elemento
    
    # in casi piu' complessi usare render_templates e quindi jsonify
    stringJson = jsonify(** dizAlunno)
    return stringJson   #aggiunge content-type => json

@app.route("/insertAlunnoPOST/", methods=["POST"])
def inserisciAlunnoPOST():
    
    numeroReg   =   request.json['numeroReg']
    nome        =   request.json['nome']
    cognome     =   request.json['cognome']
    annoNascita =   request.json['annoNascita']
    
    print [numeroReg,nome,cognome,annoNascita]
    #apre connessione al DB per inserire un Alunno
    
    conn = sqlite3.connect(pathDb)
    print "Opened database successfully";
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registroAlunni \
        (NUMEROREG,NOME,COGNOME,ANNONASCITA) \
        VALUES (?,?,?,?)",[numeroReg,nome,cognome,annoNascita]);
    conn.commit()
    conn.close()
    return jsonify("")
    
if __name__ == "__main__":
    #app.debug=True
    app.run( port=5024)


