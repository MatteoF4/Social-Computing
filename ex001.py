import sqlite3

con = sqlite3.connect('/home/matteo/Desktop/VSC Projects/Social Computing/minisocial_database.sqlite')

cur = con.cursor()

cur.execute('SELECT name FROM sqlite_master WHERE type="table";')
tables = cur.fetchall()

for t in tables:
    t_info = cur.execute('SELECT * FROM ' + t[0] + ' LIMIT 5;')
    res = t_info.fetchall()
    print(t[0])
    print(res)
    print("")

con.close()
