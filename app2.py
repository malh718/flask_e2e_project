from flask import Flask, render_template
from db import Base, Patient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(12)

# Create a SQLAlchemy engine and session
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index2():
    # Retrieve data from the database
    patients = session.query(Patient).all()
    return render_template('index_tailwind.html', patients=patients)


if __name__ == '__main__':
    app.run(
        debug=True, 
        port=5000
    )
