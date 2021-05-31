from flask import Flask, request, jsonify
from OpenSSL import SSL
import werkzeug

app = Flask(__name__)

@app.route("/") #start seite von www.was-auch-immer.de
def index():
    return "Hello World"

@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound(e):
    return jsonify(error= str(e)), e.code
    #return str(e.code)

if __name__ == '__main__':
    #threaded=True für mehrere gleichzeitige Anfragen
    app.run(port=1337, debug=True, threaded=True)
