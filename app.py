from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, World!'

# Ensure that the application context is set
with app.app_context():
    db.create_all()  # Create database tables

if __name__ == '__main__':
    app.run(debug=True)

