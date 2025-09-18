import sqlite3
import pandas as pd
import os

#clear console
os.system('clear')

DB_FILE = "minisocial_database.sqlite"

try:
    conn = sqlite3.connect(DB_FILE)
    print(f"Connection to database: {DB_FILE} succesful\n" )
except Exception as e:
    print(f"Error connecting to database: {e}")

locations = pd.read_sql_query("SELECT location, count(location) FROM users GROUP BY location ORDER BY 2 DESC LIMIT 5", conn)

print(locations)

exit()
