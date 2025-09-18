"""
You’re the social media manager of @WildHorse. For each month since @WildHorse 
registered, calculate how many comments they received total. Plot the cumulative values 
(time on X axis, number of comments on the Y axis). Based on the historical growth 
rate, predict how many months until the total number of comments on their posts 
reaches 200.
"""

import matplotlib.pyplot as plt
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

monthly_comments =  pd.read_sql_query("""
SELECT 
    strftime('%Y-%m', comments.created_at) AS year_month,
    COUNT(comments.id) AS total_comments
FROM
    posts                                      
JOIN
    comments
ON
    posts.id = comments.post_id
WHERE
    posts.user_id = (SELECT id FROM users WHERE username='WildHorse') 
GROUP BY
    year_month
""", conn)

conn.close()

plt.plot(monthly_comments['year_month'], monthly_comments['total_comments'])

plt.gcf().canvas.manager.set_window_title("Users' Comments Plot")
plt.title('Monthly comments on @WildHorse posts')
plt.xlabel('Month')
plt.ylabel('Comments')
plt.xticks(rotation=45)
plt.grid(True)

plt.show()
