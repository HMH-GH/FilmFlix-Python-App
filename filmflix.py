import sqlite3

def create_table():
  conn = sqlite3.connect('filflix.db')
  c = conn.cursor()
  c.execute()