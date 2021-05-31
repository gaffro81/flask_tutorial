from flask import Flask, request
from OpenSSL import SSL

context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_certificate('mycert.crt')
context.use_privatekey('myprivatekey.key')


app = Flask(__name__)

@app.route("/") #start seite von www.was-auch-immer.de
def index():
    return "Hello World"

if __name__ == '__main__':
    #threaded=True für mehrere gleichzeitige Anfragen
    app.run(port=1337, debug=True,  ssl_context = context, threaded=True)
