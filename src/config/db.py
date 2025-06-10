import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

# db connections for user management
DB_CONN_STR = os.getenv("DB_CONN_STR")

metadata = MetaData()
engine = create_engine(DB_CONN_STR)
conn = engine.connect()
