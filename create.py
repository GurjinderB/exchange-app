from application._init_ import db

db.drop_all()
db.create_all()