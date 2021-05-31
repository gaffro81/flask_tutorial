from flask import Flask

app = Flask(__name__)

@app.route("/") #start seite von www.was-auch-immer.de
def index():
    return "Hello World"


@app.route("/hello") #seite darunter seite von www.was-auch-immer.de/hello
def hello():
    return "Hello World"
 
@app.route("/name/<string:name>") #seite darunter seite von www.was-auch-immer.de/variable
def naming(name):
    return "Hello " + name

@app.route("/name/<path:name>") #mit path variable
def path(name):
    return "Hello " + name

if __name__ == '__main__':
    app.run(port=1337, debug=True)

