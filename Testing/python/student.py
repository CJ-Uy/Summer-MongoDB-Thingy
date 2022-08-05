import pandas as pd

from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
SECRET_KEY = os.getenv("SECRET_KEY")
connect(host=DB_HOST)

#### Not gonna lie idk where this file is supposed to be in the directory ###
import sys
sys.path.append("../../")
from . import db

print(db.getCollectionNames())