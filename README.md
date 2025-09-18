import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Optional for clearing the terminal at each run
import os
os.system('clear')

DB_FILE = "minisocial_database.sqlite"
try:
    conn = sqlite3.connect(DB_FILE)
except Exception as e:
    print(f"Couldn't connect to the Database: '{e}'")

try: # SQL code
    print('*'*32)
    
except Exception as e:
    print(f"Error while loading data: '{e}'")
finally:
    if conn:
        conn.close()
        
