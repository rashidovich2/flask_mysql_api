from flask import Flask
from flask_restful import Api
from resources import UserResource

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
api = Api(app)

# Load environment variables from .env file
load_dotenv()
db_uri = os.getenv('SQLALCHEMY_DATABASE_FULL_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

api.add_resource(UserResource, '/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)