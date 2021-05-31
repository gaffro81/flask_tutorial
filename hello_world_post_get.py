from flask import Flask, url_for, request
from flask.templating import render_template

app = Flask(__name__)
 
@app.route("/") #
def index():
    return render_template('index.html', variable1="Das ist cool!!!")

@app.route("/login", methods=['POST'])
def login():
    name = ''
    if request.method == 'POST':
        name = request.form['name1']
    else:  
        name = request.args('name1')
    return "hello " + name

if __name__ == '__main__':
    app.run(port=1337, debug=True)