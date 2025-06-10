import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

# db connections for user management
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")
# DB_USERNAME = os.getenv("DB_USERNAME")
# DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_CONN_STR = os.getenv("DB_CONN_STR")

metadata = MetaData()
engine = create_engine(DB_CONN_STR)
conn = engine.connect()
