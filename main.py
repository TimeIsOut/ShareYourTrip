#adding libries
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import defaultload
from datetime import datetime


#site config
app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__ (self):
        return '<Article %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)