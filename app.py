from flask import Flask, render_template, url_for, redirect, session
from db import Base, Patient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd 
import os
from db_functions import update_or_create_user

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)



@app.route('/')
def index():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html',current_datetime=current_datetime, formatted_date=formatted_date)

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ###note, if running locally on a non-google shell, do not need to override redirect_uri
    ### and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ##, note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    redirect_uri = 'https://5000-cs-741144739238-default.cs-us-east1-vpcf.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route("/about")
def table():

    data_dic = {
        'Patient ID': [45103, 87126, 34980, 56201, 91032, 65487, 23716],
        'Cancer type': ['Leukemia', 'Breast Cancer', 'Prostate Cancer', 'Colon Cancer', 'Ovarian Cancer', 'Pancreatic Cancer', 'Lung Cancer'],
        'First Name': ['Liam', 'Emma', 'Noah', 'Olivia', 'Ava', 'Isabella', 'Sophia'],
        'Last Name': ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller'],
        'Date of Birth': ['04/17/89', '12/05/92', '09/22/84', '07/13/95', '03/28/91', '11/08/87', '06/01/90'],
        'Part of Long Island': ['Hicksville', 'Garden City', 'Massapequa', 'Port Washington', 'Huntington', 'Smithtown', 'Freeport'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Female','Male']
        
    }
    columns = ['Patient ID', 'Cancer type', 'First Name','Last Name','Date of Birth', 'Part of Long Island', 'Gender']
    index = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g']

    df = pd.DataFrame(data_dic, columns=columns, index=index)
    table = df.to_html(index=False)
    
    return render_template(
        "about.html",
        table=table)   
    

if __name__ == '__main__':
    #app.run(
       # debug=True, 
           app.run(debug=True, host='0.0.0.0')
       # port=5000
    #)