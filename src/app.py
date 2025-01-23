from flask import Flask, render_template, request, redirect, url_for
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])

        return 'Datos procesados'

    else:
        return render_template('auth/login.html')
    



if __name__ == '__main__':

    app.config.from_object(config['development'])
    app.run()