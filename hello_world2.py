from flask import Flask, url_for

app = Flask(__name__)
 
@app.route("/") #
def index():
    return '<a href=' + url_for("path", name = "Dirk") + '>Lass dich grüßen</a>'  
    #url_for first argument is function (in this case: path)
    #url_for second argument is argument (in this case: name)

@app.route("/hello/<name>") #mit path variable
def path(name):
    return "Hello " +name

if __name__ == '__main__':
    app.run(port=1337, debug=True)
