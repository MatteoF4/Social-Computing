import matplotlib as plt
import pandas as pd
import sqlite3

# Optional for clearing the terminal at each run
import os
os.system('clear')

DB_FILE = "minisocial_database.sqlite"
try:
    conn = sqlite3.connect(DB_FILE)
    print("SQLite Database connection successful")
except Exception as e:
    print(f"Couldn't connect to the Database: '{e}'")

user_reactions_df = pd.read_sql_query("""
                                SELECT 
                                    user_id, 
                                    COUNT(post_id) AS reacts
                                FROM 
                                    reactions 
                                GROUP BY 
                                    post_id;
                                """
                                  , conn)

print(user_reactions_df)

