from flask import Flask, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/VickyQian'
db = SQLAlchemy(app)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33509)
  
