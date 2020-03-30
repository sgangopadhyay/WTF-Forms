from flask import Flask, url_for, render_template
from flask import request
from flask_wtf import Form 
from wtforms import TextField
from wtforms import PasswordField
from wtforms import SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'suman@123'

class UserForm(Form):
    username = TextField("Name of User :")
    password = PasswordField("Enter Password :")
    submit = SubmitField("Enter Data")

@app.route('/', methods = ['GET', 'POST'])
def wtf():
    form = UserForm()
    if request.method == 'POST':
        return render_template('display.html')
    return render_template('wtf.html', form = form)

def display():
    pass 

if __name__ == '__main__':
    app.run(debug=True, port = 8080)