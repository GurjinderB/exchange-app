from flask import redirect, render_template, url_for, request
from application._init_ import app, db
from application.models import Account, Coin, Transaction
from application.forms import AddUser, Transaction
import numpy as np
#from datetime import date, timedelta

@app.route('/', methods=['GET', 'POST'])
def home():
    #data = db.session.execute(f"SELECT name FROM account WHERE desc LIKE '%{name}%'")
    global btc, eth
    btc = round(29714 * (1+ np.random.normal(loc=0, scale=0.05)), 2)
    eth = round(1962 * (1+ np.random.normal(loc=0, scale=0.1)), 2)
    return render_template('index.html', btc=btc, eth=eth)

@app.route('/create/<name>')
def createcoin(name):
    coin = Coin(name=name)
    db.session.add(coin)
    db.session.commit()
    return 'Done'

@app.route('/create-account', methods=['GET', 'POST'])
def create_user():
    form = AddUser()
    if request.method == 'POST':
        name = form.name.data
        username = form.username.data
        deposit = form.balancegbp.data
        new_user = Account(name=name, username=username, balancegbp=deposit)
        db.session.add(new_user)
        db.session.commit()   
    return render_template('create_account.html', form=form)
    
@app.route('/create-order', methods=['GET', 'POST'])
def create_order():
    coins = Coin.query.all()
    form = Transaction()
    if request.method == 'POST':
        type = form.type.data
        amount = form.amount.data
        submit = form.submit.data
        db.session.add()
        db.session.commit()
    return render_template('create_order.html', btc=btc, eth=eth, form=form)

@app.route('/delete/<username>')
def delete(username):
    user = Account.query.get(username)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/transaction-history')
def show_tranactions():
    pass