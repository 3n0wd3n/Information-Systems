from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite3"
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

@app.route('/')
def all():
    return render_template('all.html', dates = Date.query.all())
    # Date.query.filter_by(day=1, month=5).all()

@app.route('/new', methods = ['POST', 'GET'])
def new():
    if request.method=='POST':
        date = Date(int(request.form['day']),
                    int(request.form['month']),
                    request.form['name'])
        db.session.add(date)
        db.session.commit()
        return redirect(url_for('all'))
    else:
        return render_template('new.html')

db.create_all()    
app.run()
