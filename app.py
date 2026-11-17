from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from database import db
from flask_jwt_extended import JWTManager
import os 

load_dotenv()

api = Flask(__name__)

api.config['UPLOAD_FOLDER']='.static/fotos/'

cors=CORS(api,resources={r"/estatic/*":{"origins":"*"},
                        r"/api/*":{"origins":"*"}
                        })

DB_USER = os.getenv("DB_USER")
DB_NAME=os.getenv("DB_NAME")
DB_PORT=os.getenv("DB_PORT")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")

api.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

api.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(api)

jwt=JWTManager(api)

if __name__ == '__main__':
    with api.app_context():
        db.create_all()
    api.run(port=5000, debug=True)