# imports
from flask import Flask, render_template, request, redirect, jsonify, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from passlib.hash import sha256_crypt
from dotenv import load_dotenv
from datetime import datetime
import os

# config
app = Flask(__name__)
# env variable
load_dotenv()
# variables
app.secret_key = os.getenv("SECRET_KEY")
host = os.getenv("HOST")
port = os.getenv("PORT")

# Landing page
@app.route('/')
def landing():
    return render_template("index.html")



# Run app
if __name__ == "__main__":
    # app.run(debug=True, host=host, port=port)
    app.run()
