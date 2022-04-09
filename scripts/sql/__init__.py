import psycopg2 as pg
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

db = os.environ.get("POSTGRE_DB")
user = os.environ.get("POSTGRE_USER")
password = os.environ.get("POSTGRE_PASS")
host = os.environ.get("POSTGRE_HOST")
port = os.environ.get("POSTGRE_PORT")

conn = pg.connect(database=db, user=user, password=password, host=host, port=port)
cursor = conn.cursor()