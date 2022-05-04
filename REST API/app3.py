from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Date(db.Model):
    id = db.Column('date_id', db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    name = db.Column(db.String(100))

    def __init__(self, day, month, name):
        self.day = day
        self.month = month
        self.name = name

    def to_dict(self):
        return {"day": self.day,
                "month": self.month,
                "name": self.name,
                "id": self.id}

@app.route('/')
def index():
    return "Hello!"

@app.route('/holidays')
def get_holidays():
    dates = Date.query.all()
    result = [d.to_dict() for d in dates]
    return {"holidays": result}

@app.route('/holidays', methods=['POST'])
def add_holiday():
    date = Date(int(request.json['day']),
                int(request.json['month']),
                request.json['name'])
    db.session.add(date)
    db.session.commit()
    return {"id": date.id}

@app.route('/holidays/<id>')
def get_holiday(id):
    date = Date.query.get(id)
    if date == None:
        return {"error":"not found"}
    return date.to_dict()

@app.route('/holidays/<id>', methods=['DELETE'])
def delete_holiday(id):
    date = Date.query.get(id)
    if date == None:
        return {"error":"not found"}
    db.session.delete(date)
    db.session.commit()
    return {"message":"OK"}

@app.route('/holidays/<id>', methods=['PUT'])
def update_holiday(id):
    pass

#db.create_all()  
app.run()
