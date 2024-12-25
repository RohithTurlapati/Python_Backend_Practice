from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
# db.init_app(app)
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(100))

    def __repr__(self):
        return '<Drink %r>' % self.id



@app.route("/")
def index():
    return "Hello world"

@app.route("/addDrink/<name>/<desc>", methods=['POST'])
def addDrink(name, desc):
    drink = Drink(name=name,description=desc)
    print(drink)
    db.session.add(drink)
    db.session.commit()
    return {"Drink ID": drink.id}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)