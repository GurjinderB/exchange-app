from application._init_ import db

class Account(db.Model):
    pkuserid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_name = db.Column(db.String(50))
    balancegbp = db.Column(db.Float)
    transaction = db.relationship('Transaction', backref='account')

class Coin(db.Model):
    pkcoinid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5))
    price = db.Column(db.Float)
    transaction = db.relationship('Transaction', backref='coin')

class Transaction(db.Model):
    pktransactionid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(4))
    coinid = db.Column('coin_pkcoinid', db.Integer, db.ForeignKey('coin.pkcoinid'))
    userid = db.Column('accoint_pkuserid', db.Integer, db.ForeignKey('account.pkuserid'))
