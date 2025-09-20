from flask_sqlalchemy  import SQLAlchemy


#instantiate sqlalchemy
db =SQLAlchemy()

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String )

class Items(db.Model):
    __tablename__ ='items'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String )
    price= db.Column(db.Float)