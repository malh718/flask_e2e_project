from flask import Flask, render_template
from db import Base, Patient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# # Create a SQLite database (you can change this to your specific database)
# # DATABASE_URL = "mysql+pymysql://hants:ahi-admin-2023@scratch-server.mysql.database.azure.com/hants"
DATABASE_URL = "mysql+mysqldb://mnh:mnh@34.31.63.12:3306/local.db"
DATABASE_URL = "sqlite:///local.db"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
Base.metadata.bind = app

# Create a SQLAlchemy engine and session
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    # Retrieve data from the database
    patients = session.query(Patient).all()
    return render_template('index_tailwind.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)