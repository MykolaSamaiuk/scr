import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#sql
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///datab.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Persons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    data_pas = db.Column(db.String(200), unique=True, nullable=False)
    cash = db.Column(db.Integer, nullable=False)
    description_tovaru = db.Column(db.String(250), unique=True, nullable=False)
    
def __init__(self, name, data_pas, cash, description_tovaru):
         self.name
         self.data_pas
         self.cash
         self.description_tovaru 

def __str__(self):
        return f'({self.id},{self.name},{self.data_pas},{self.cash},{self.description_tovaru})'


class Tovar(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False )
    title = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)

def __str__(self):
        return f'({self.title},{self.price},{self.description})'
   
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#@app.after_request
#def after_request(response):
#    """Ensure responses aren't cached"""
#    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#    response.headers["Expires"] = 0
#    response.headers["Pragma"] = "no-cache"
#    return response


@app.route('/')
@app.route('/home')
def index():
    tovars = Tovar.query.all()
    return render_template("index.html", tovars=tovars)


@app.route("/produkt/info", methods=["GET", "POST"])
def info():
    users = Persons.query.all()
    return render_template("baseapp.html", users = users)


@app.route('/produkt', methods = ['GET', 'POST'])
def produkt():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['data_pas'] or not request.form['cash']:
         flash('Перевірте коректність даних', 'error')
      else:
         users = Persons(request.form['name'], request.form['data_pas'],
            request.form['cash'], request.form['description_tovaru'])
        
         db.session.add() 
         db.session.commit()
         flash('cool..')
         return redirect('/produkt/info')
   return render_template('produkt.html')


@app.route('/about')
def about():
    return render_template("about.html")

    
@app.route('/prav')
def prav():
    return render_template("prav.html")


@app.route('/klient')
def klient():
    users = Persons.query.all()
    return render_template("klient.html", users=users)


@app.route('/tovar')
def tovar():
    tovars = Tovar.query.all()
    return render_template("tovar.html", tovars=tovars)
    session.close()


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

    