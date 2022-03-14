from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField

class AddUser(FlaskForm):
    name = StringField('Name: ')
    username = StringField('User Name: ')
    balancegbp = FloatField('Initial Deposit: ')
    submit = SubmitField('Create account')
    
class Transaction(FlaskForm):
    type = SelectField('Transaction Type: ', choices=[('buy', 'buy'), ('sell', 'sell')])
    amount = FloatField('Amount to spend: ')
    coinid = SelectField('Select a coin: ', choices=[('Bitcoin', 'btc'), ('Ethereum', 'eth')])
    userid = IntegerField('User making transaction: ')
    submit = SubmitField('Create order')

    