import psycopg2 as pg
import dotenv
import os

class Connector():
    def __init__(self):
        self.db = os.environ["DATABASE_URL"]
        self.conn = pg.connect(database=self.db)
        self.cursor = self.conn.cursor()
    def drop_and_create(self):
        self.tables = ["type1", "type2", "type3", "type4", "type5", "type6", "type7", "type8"] 
        queries = []
        for i in self.tables:
            queries.append("DROP TABLE IF EXISTS {i}")
        for i in self.tables:
            queries.append(f"CREATE TABLE {i}(plot text, type int")
        for i in queries:
            self.cursor.execute(i)
            self.cursor.commit()
    def insert(self, type, queries):
        for i in queries:
            self.cursor.execute("INSERT INTO ? (plot, type) VALUES(%s, %s)", queries)
            self.cursor.commit()
