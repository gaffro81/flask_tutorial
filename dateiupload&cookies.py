from flask import Flask, url_for, request, redirect
from flask.helpers import make_response
from flask.templating import render_template
import os
from werkzeug.utils import secure_filename


folder = "upload/in"
extensions = set(['txt','jpg'])

def allowed(filename):
    return any([ True if filename.split('.')[1].lower() == ext else False for ext in extensions])

#print(allowed('test.txt'))


# flask app

app = Flask(__name__)
 
@app.route("/", methods=['GET','POST' ]) #
def index():
    if request.method == 'POST':
        if 'uploadfile' not in request.files:
            return redirect(request.url)
        file = request.files['uploadfile']
        if file.filename == '':
            return redirect(request.url)
        if allowed(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return "<h1>Upload erfolgreich</h1>"
        else:
            return redirect(request.url)
    return '''
    <h1>Upload</h1>
    <form method=post enctype=multipart/form-data>
        <input type= file name = uploadfile>
        <input type= submit name = Hochladen>
    </form>

    '''

#Aufruf mit http://127.0.0.1:1337/login?name1=Dirk
@app.route("/login", methods=['POST', 'GET'])
def login():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return "Hallo " + cookie
    name = ''
    if request.method == 'POST':
        name = request.form['name1']
    else:  
        name = request.args.get('name1')
    resp = make_response("Hello " + name + "!")
    resp.set_cookie('username', name)
    return resp

if __name__ == '__main__':
    app.run(port=1337, debug=True)
