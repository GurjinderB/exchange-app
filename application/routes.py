from flask import redirect, render_template, url_for, request
from application._init_ import app, db
from application.models import Account, Coin, Transaction
from application.forms import AddUser, Transaction
import numpy as np
#from datetime import date, timedelta

@app.route('/')
def home():
    btc = round(29714 * (1+ np.random.normal(loc=0, scale=0.1)), 2)
    eth = round(1962 * (1+ np.random.normal(loc=0, scale=0.1)), 2)
    return render_template('index.html', btc=btc, eth=eth)
    #return f"{Account.query.count()} accounts: " + '<br>'.join(str(t) + " " + str(t.coin) for t in Account.query.all())

@app.route('/create/<name>/<price>')
def createcoin(name, price):
    coin = Coin(name=name, price=price)
    db.session.add(coin)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/create-account', methods=['GET', 'POST'])
def createuser():
    form = AddUser()
    if request.method == 'POST':
        name = form.name.data
        username = form.username.data
        deposit = form.balancegbp.data
        new_user = Account(name=name, username=username, balancegbp=deposit)
        db.session.add(new_user)
        db.session.commit()   
    return render_template('create_account.html', form=form)
    

