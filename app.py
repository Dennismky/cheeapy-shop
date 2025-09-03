from flask import Flask;

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cheeapyshop.db'

db.init_app(app)
migrate = Migrate(app,db)


if __name__ == '__main__':
    app.run()
    degug="True"
