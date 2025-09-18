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
except Exception as e:
    print(f"Couldn't connect to the Database: '{e}'")

# Retrieve tables' data as Pandas DataFrames
try:
    users = pd.read_sql_query("SELECT * FROM users", conn)
    posts = pd.read_sql_query("SELECT * FROM posts", conn)
    comments = pd.read_sql_query("SELECT * FROM comments", conn)
except Exception as e:
    print(f"Error while loading data: '{e}'")
finally:
    if conn:
        conn.close()

print('*'*32)

# Find WildHorse's user_id
wh_row = users.loc[users['username'] == 'WildHorse']
wh_id = wh_row['id'].iloc[0]

# Retrieve all WildHorse's posts' ids
wh_posts_ids = posts.loc[posts['user_id'] == wh_id, 'id']

# Retrieve all comments on any WildHorse's posts
wh_comments = comments[comments['post_id'].isin(wh_posts_ids)].copy()

# Restrict the comments' data as dates and format them from 
# 'YYYY-MM-DD hh:mm:ss' to 'YYYY-MM', so their first 7 characters

wh_comments['month'] = wh_comments['created_at'].str[:7]

# Count each month's number of comments
monthly_comments = wh_comments.groupby('month').size()

# Turn the result into a DataFrame
results = monthly_comments.reset_index(name='monthly_comments')

# Sort the timeline by month
results = results.sort_values('month')

#results['cumulative_comments'] = results['monthly_comments'].cumsum()
#print(results)

# Plot the results
plt.plot(results['month'], results['monthly_comments'])

plt.gcf().canvas.manager.set_window_title("Users' Comments Plot")
plt.title('Monthly comments on @WildHorse posts')
plt.xlabel('Month')
plt.ylabel('Comments')
plt.xticks(rotation=45)
plt.grid(True)

plt.show()
