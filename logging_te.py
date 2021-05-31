from flask import Flask

app = Flask(__name__)

@app.route("/") #start seite von www.was-auch-immer.de
def index():
    app.logger.info("einmal ausgeführt")
    return "Hello World"

if __name__ == '__main__':
    #threaded=True für mehrere gleichzeitige Anfragen
    app.run(port=1337, debug=True, threaded=True)
