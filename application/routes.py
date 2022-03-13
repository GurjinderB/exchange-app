from flask import redirect, render_template, url_for
from application._init_ import app, db
from application.models import Account, Coin, Transaction
from datetime import date, timedelta

@app.route('/')
def home():
    return render_template('index.html')
    #return f"{Account.query.count()} accounts: " + '<br>'.join(str(t) + " " + str(t.coin) for t in Account.query.all())

@app.route('/create/<name>/<price>')
def createcoin(name, price):
    coin = Coin(name=name, price=price)
    db.session.add(coin)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/create/account/<name>/<username>/<deposit>')
def createuser(name, username, deposit):
    user = Account(name=name, username=username, balancegbp=deposit)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))

