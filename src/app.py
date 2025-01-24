from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL

#MODELS
from models.ModelUser import ModelUser

#ENTITIES
from models.entities.User import User

app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(0, username, password)

        logged_user = ModelUser.login(db, user)

        if logged_user:        
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                flash('Invalid password')
                return render_template('auth/login.html')
        
        else:
            flash('User not found...')

            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')
    
@app.route('/home')
def home():

    return render_template('home.html')

if __name__ == '__main__':

    app.config.from_object(config['development'])
    app.run()