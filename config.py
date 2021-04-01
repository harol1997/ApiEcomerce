from dotenv import load_dotenv
from os import getenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

host = getenv('DATABASE_HOST')
port = getenv('DATABASE_PORT')
db = getenv('DATABASE_NAME')
user = getenv('DATABASE_USER')
password = getenv('DATABASE_PASS')

class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY =  getenv('SECRET_KEY')
    