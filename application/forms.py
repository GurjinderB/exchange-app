from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField

class AddUser(FlaskForm):
    name = StringField('Name: ')
    username = StringField('User Name: ')
    balancegbp = FloatField('Initial Deposit: ')

class Transaction(FlaskForm):
    type = SelectField('Transaction Type: ', choices=[('buy', 'buy'), ('sell', 'sell')])
    coinid = SelectField('Transaction Type', choices=[('Bitcoin', 'BTC'), ('Ethereum', 'ETH')])
    userid = IntegerField('User making transaction')
    submit = SubmitField('Create account')