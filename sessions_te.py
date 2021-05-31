from flask import Flask, url_for, request, redirect, session, escape
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

app.secret_key = '1234'

@app.route("/logout")
def logout():
    session.pop('name', None)
    return redirect(url_for('sessions'))


@app.route("/", methods=['GET','POST' ]) #
def sessions():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(request.url)
    else:
        if 'name' in session:
           # return '<a href=' + url_for("logout") + '>' +escape(session['name'])+ '</a>'
           test = str(escape(session['name']))
           return '<a href=' + url_for("logout") + '>'+ test +'</a>'
        else:
            return '''
            <h1>Login</h1>
            <form method=post>
                <input type= text name = name>
                <input type= submit name = Login>
            </form>

            '''




if __name__ == '__main__':
    app.run(port=1337, debug=True)
