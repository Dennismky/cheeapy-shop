from flask import Flask,make_response, redirect, abort, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db

# instantiate flask app
app= Flask(__name__)

# configure our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cheeapy.db'
db.init_app(app)
migrate= Migrate(app, db)

@app.route('/')
def welcome():
    resp_body= "<h1>welcome</H1>"
    resp_code= 200
    resp= make_response(resp_body,resp_code)
    return resp
    
@app.route('/logout')
def logout():
    return "<h1>bye</h1>", 201

@app.route('/welcome')
def welcome():
    resp_body="<h1>welcome</h1>"  
    resp_code=200
    resp= make_response(resp_body, resp_code)
    return resp  

if __name__ == '__main__':
    app.run(),
    debug="True"
