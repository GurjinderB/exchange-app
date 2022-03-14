from application._init_ import db

class Account(db.Model):
    pkuserid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50))
    balancegbp = db.Column(db.Float)
    fktransaction = db.relationship('Transaction', backref='account')

class Coin(db.Model):
    pkcoinid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5))
    fktransaction = db.relationship('Transaction', backref='coin')

class Transaction(db.Model):
    pktransactionid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    amount = db.Column(db.Float)
    coinid = db.Column('coin_pkcoinid', db.Integer, db.ForeignKey('coin.pkcoinid'))
    userid = db.Column('account_pkuserid', db.Integer, db.ForeignKey('account.pkuserid'))
