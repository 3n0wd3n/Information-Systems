from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# object/model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(200))  
    rating = db.Column(db.Integer)

    def __init__(self, name, author, rating):
        self.name = name
        self.author = author
        self.rating = rating
        
    def to_dict(self):
        return {"id": self.id, "name":self.name,
                "author":self.author, "rating":self.rating}


# just test
@app.route('/')
def index():
    return "Hello!"

# create database file
def create_data():
    db.create_all()
    books = [Book("The Martian", "Andy Weir", 5),
             Book("Artemis", "Andy Weir", 3),
             Book("The Wool", "Hugh Howey", 5)]
    for b in books:
        db.session.add(b)
        db.session.commit()


#jen jednou v interpretu (python z cmd ve venv)
#from app import create_data
#create_data()
